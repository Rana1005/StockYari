Setup:
1. Download python in your machine
2. Create a virtual env
3. Install all the dependencies mentioned in the requirement.txt file
4. Run the server

API:
1. curl --location 'http://127.0.0.1:8000/stock_info/all_avaliable_index/'
   response:{
    "data": [
        "NIFTY 200",
        "NIFTY 50",
        "NIFTY MIDCAP 50",
        "NIFTY NEXT 50",
        "NIFTY SMALLCAP 50"
    ]
}

2.curl --location --request GET 'http://127.0.0.1:8000/stock_info/stock_past_records/?start_date=2024-01-31&end_date=2024-02-02&page=1' \
--header 'Content-Type: application/json' \
--data '{
    "open<=":110,
    "open=>":11000,
    "high<=":200,
    "high>=":200,
    "low<=":300,
    "low>=":310,
    "close>=":100,
    "close<=":200,
    "shares_traded<=":600,
    "shares_traded>=":600,
    "turnover>=":800,
    "turnover<=":500
}'

response:{
    "start-date": "2024-01-31",
    "end_date": "2024-02-02",
    "pagination": {
        "page": "1",
        "total_pages": 1,
        "total_rows": 10
    },
    "data": [
        {
            "date": "2024-01-31",
            "open": 11822.45,
            "high": 11961.5,
            "low": 11802.5,
            "close": 11953.8,
            "shares_traded": 1930336648.0,
            "turnover": 81675.18,
            "indexes": "NIFTY 200"
        },
        {
            "date": "2024-02-01",
            "open": 11992.75,
            "high": 12003.15,
            "low": 11901.2,
            "close": 11937.65,
            "shares_traded": 2240822171.0,
            "turnover": 78347.96,
            "indexes": "NIFTY 200"
        },
        {
            "date": "2024-01-31",
            "open": 21487.25,
            "high": 21741.35,
            "low": 21448.85,
            "close": 21725.7,
            "shares_traded": 410583065.0,
            "turnover": 41587.85,
            "indexes": "NIFTY 50"
        },
        {
            "date": "2024-02-01",
            "open": 21780.65,
            "high": 21832.95,
            "low": 21658.75,
            "close": 21697.45,
            "shares_traded": 332541208.0,
            "turnover": 34042.15,
            "indexes": "NIFTY 50"
        },
        {
            "date": "2024-01-31",
            "open": 13479.25,
            "high": 13633.65,
            "low": 13450.3,
            "close": 13620.6,
            "shares_traded": 456352198.0,
            "turnover": 11578.48,
            "indexes": "NIFTY MIDCAP 50"
        },
        {
            "date": "2024-02-01",
            "open": 13672.35,
            "high": 13672.35,
            "low": 13427.4,
            "close": 13529.35,
            "shares_traded": 619810209.0,
            "turnover": 13867.77,
            "indexes": "NIFTY MIDCAP 50"
        },
        {
            "date": "2024-01-31",
            "open": 54916.1,
            "high": 55346.55,
            "low": 54800.1,
            "close": 55299.25,
            "shares_traded": 467463967.0,
            "turnover": 16220.87,
            "indexes": "NIFTY NEXT 50"
        },
        {
            "date": "2024-02-01",
            "open": 55673.85,
            "high": 55858.3,
            "low": 55168.6,
            "close": 55508.85,
            "shares_traded": 481077234.0,
            "turnover": 17037.36,
            "indexes": "NIFTY NEXT 50"
        },
        {
            "date": "2024-01-31",
            "open": 7304.65,
            "high": 7441.8,
            "low": 7293.9,
            "close": 7435.4,
            "shares_traded": 659905396.0,
            "turnover": 7870.39,
            "indexes": "NIFTY SMALLCAP 50"
        },
        {
            "date": "2024-02-01",
            "open": 7483.1,
            "high": 7493.05,
            "low": 7386.0,
            "close": 7454.5,
            "shares_traded": 670680738.0,
            "turnover": 7160.84,
            "indexes": "NIFTY SMALLCAP 50"
        }
    ],
    "ranges": {
        "open": {
            "lowest": 7304.65,
            "highest": 55673.85
        },
        "high": {
            "lowest": 7441.8,
            "highest": 55858.3
        },
        "low": {
            "lowest": 7293.9,
            "highest": 55168.6
        },
        "close": {
            "lowest": 7435.4,
            "highest": 55508.85
        },
        "shares_traded": {
            "lowest": 332541208.0,
            "highest": 2240822171.0
        },
        "turnover": {
            "lowest": 7435.4,
            "highest": 55508.85
        }
    }
}
   
 
 
