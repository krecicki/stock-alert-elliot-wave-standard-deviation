# Colab Notebook
https://colab.research.google.com/drive/1pceLs9xdsibCqw7rO2Uedh-owSQPEHrF?usp=sharing

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
