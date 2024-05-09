# Colab Notebook
https://colab.research.google.com/drive/1pceLs9xdsibCqw7rO2Uedh-owSQPEHrF?usp=sharing

# The math behind the code
<p align="center">
![ql_de77f9e6a81d2a66256f61a42231d4bd_l3](https://github.com/krecicki/stock-alert-standard-deviation-scanner/assets/42053642/9d0c8994-53e2-44b9-b828-1ea010d847c2)

![ql_fb71b24349110fcafe6864565d3b53be_l3](https://github.com/krecicki/stock-alert-standard-deviation-scanner/assets/42053642/44055927-50dd-4e8a-8325-3c9e1e2dc3a6)

![ql_8c33340f20a2b2705f1c911adfdb649f_l3](https://github.com/krecicki/stock-alert-standard-deviation-scanner/assets/42053642/9bff8657-3e42-4036-aca5-74fc34f783ba)

![ql_746897a26285de696305a155858a23e4_l3](https://github.com/krecicki/stock-alert-standard-deviation-scanner/assets/42053642/a279c475-8aa9-444c-a7f8-6e3f887c8495)
</p>

# stock-alert-standard-deviation
Using σ/+2σ standard deviations to notify when to buy, sell hold individual stock tickers.

This script will output the stock ticker’s current status regarding the -2σ/+2σ range based on a list of companies in the NASDAQ in a list of outliers.

# Back story on this quant indicator 
Someone on Twitter who does quant trading told me, "Asness says anything that has a price can be trend followed. at fundamental level buying from -2σ and selling over +2σ works well on commodities. you can combine it with seasonality, calendar or day of the week anomalies etc. depending on your trading horizon."

Cliff Asness, a notable figure in finance, suggests that trend following can be applied to any asset that has a price. This is based on the idea that prices tend to move in trends over time, and these trends can be capitalized on through strategic buying and selling.

At a fundamental level, buying at -2 standard deviations (σ) and selling over +2σ refers to a statistical approach where you enter a trade when the price is significantly below its mean (suggesting it’s undervalued) and exit when it’s significantly above its mean (indicating it’s overvalued). This is particularly noted to work well with commodities, which often exhibit mean-reverting behavior.

# Sample output
Tickers more than 2σ below the mean (buy these): 
['AIRT', 'AKTS', 'ALGN', 'AMPL', 'AMRK', 'ANDE', 'ANSCU', 'APM', 'APYX', 'ARQQW', 'ARTW', 'ATEC', 'AVDL', 'BBLGW', 'CERT', 'CISO', 'CNGLU', 'CSTE', 'CVIIU', 'CYRX', 'CYTO', 'DH', 'EYE', 'FLYW', 'FTAIO', 'GANX', 'GLBE', 'GO', 'IAS', 'INAQW', 'IXAQ', 'LIFWW', 'LZ', 'MASI', 'MCRB', 'MIND', 'NATR', 'NRC', 'ODP', 'ONYX', 'OXLCL', 'PDYNW', 'POWW', 'PYPD', 'QLYS', 'REFI', 'RMR', 'RPD', 'RRR', 'SHLS', 'SHPW', 'SLAMU', 'SMLR', 'SSYS', 'STAA', 'SVC', 'TMCI', 'TRIP', 'TRVI', 'UK', 'VOXX', 'YHGJ', 'ZI', 'ZLS']

Tickers more than 2σ above the mean (sell these): 
['AENT', 'AFAR', 'AFJKU', 'ALPN', 'AMED', 'AOSL', 'APEI', 'ARKO', 'ASTI', 'ATER', 'BAYA', 'BAYAU', 'BLAC', 'BRLS', 'BRP', 'CCGWW', 'CCTG', 'CFBK', 'CFLT', 'CITE', 'CLOE', 'CLVR', 'CNSP', 'CODA', 'CRCT', 'CRUS', 'CSCO', 'DMTK', 'ERNA', 'FREE', 'FRLAW', 'FRSX', 'GAN', 'GATE', 'HAIAU', 'HCVI', 'HSII', 'IEP', 'IMAQU', 'IMNN', 'INGN', 'INOD', 'INTA', 'IRBT', 'ISPOW', 'ISUN', 'JVSAU', 'JZ', 'KTCC', 'LASE', 'LFWD', 'LGND', 'LIQT', 'LIXTW', 'LPRO', 'MINDP', 'MXCT', 'MYGN', 'NUKK', 'NVAC', 'OCEA', 'OXBR', 'PAYO', 'PCRX', 'PFTA', 'PLMI', 'PLMJ', 'POWI', 'PPSI', 'PPYA', 'PRLH', 'RDWR', 'REBN', 'REFR', 'RSSS', 'SATL', 'SCRMU', 'SEED', 'SENEB', 'SGC', 'SLNH', 'SNCR', 'SPNS', 'SQFTP', 'SSTI', 'SWIM', 'SWSS', 'SY', 'TH', 'THMO', 'TIGO', 'TIVC', 'YOSH', 'YS']

Top 10 by Volume:
CPOP: 56273872
CTMX: 15732692
NTBL: 7644933
ABNB: 5316625
TIVC: 5316430
CDLX: 4191264
CYN: 4027743
BMBL: 2833685
SEDG: 2483079
GTHX: 2449504
