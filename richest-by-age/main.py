import matplotlib.pyplot as plt

# $('#the_list').find('tr').find('td:eq(0), td:eq(4)').remove() // run on https://www.forbes.com/billionaires/list/#version:realtime

s = """#1	Jeff Bezos	$143.5 B	54	Amazon	United States
	#2	Bill Gates	$93.5 B	62	Microsoft	United States
	#3	Warren Buffett	$81.8 B	87	Berkshire Hathaway	United States
	#4	Bernard Arnault	$80.7 B	69	LVMH	France
	#5	Mark Zuckerberg	$77.2 B	34	Facebook	United States
	#6	Amancio Ortega	$75.7 B	82	Zara	Spain
	#7	Carlos Slim Helu	$66.7 B	78	telecom	Mexico
	#8	Larry Ellison	$57.7 B	73	software	United States
	#9	Larry Page	$53.5 B	45	Google	United States
	#10	Michael Bloomberg	$52.2 B	76	Bloomberg LP	United States
	#11	Sergey Brin	$52 B	44	Google	United States
	#12	Charles Koch	$51.2 B	82	Koch Industries	United States
	#12	David Koch	$51.2 B	78	Koch Industries	United States
	#14	Francoise Bettencourt Meyers	$48.3 B	65	L'Oreal	France
	#15	Mukesh Ambani	$42.5 B	61	petrochemicals, oil & gas	India
	#16	Ma Huateng	$42.2 B	46	internet media	China
	#17	Jim Walton	$41.8 B	70	Walmart	United States
	#18	S. Robson Walton	$41.5 B	73	Walmart	United States
	#19	Alice Walton	$41.5 B	68	Walmart	United States
	#20	Sheldon Adelson	$40.9 B	84	casinos	United States
	#21	Jack Ma	$40.9 B	53	e-commerce	China
	#22	Steve Ballmer	$39.8 B	62	Microsoft	United States
	#23	Phil Knight	$33.8 B	80	Nike	United States
	#24	Francois Pinault	$33.8 B	81	luxury goods	France
	#25	Li Ka-shing	$32.8 B	90	diversified	Hong Kong
	#26	Hui Ka Yan	$29.3 B	59	real estate	China
	#27	Lee Shau Kee	$29 B	90	real estate	Hong Kong
	#28	Wang Jianlin	$29 B	63	real estate	China
	#29	Beate Heister & Karl Albrecht Jr.	$28.9 B	66	supermarkets	Germany
	#30	Jorge Paulo Lemann	$26.9 B	78	beer	Brazil
	#31	David Thomson	$25.8 B	61	media	Canada
	#32	Dietrich Mateschitz	$25.4 B	74	Red Bull	Austria
	#33	Jacqueline Mars	$25.2 B	78	candy, pet food	United States
	#33	John Mars	$25.2 B	82	candy, pet food	United States
	#35	Michael Dell	$24.1 B	53	Dell computers	United States
	#36	Leonardo Del Vecchio	$23.2 B	83	eyeglasses	Italy
	#37	Yang Huiyan	$23.1 B	36	real estate	China
	#38	Susanne Klatten	$23 B	56	BMW, pharmaceuticals	Germany
	#39	Masayoshi Son	$22.2 B	60	internet, telecom	Japan
	#40	Tadashi Yanai	$21.8 B	69	fashion retail	Japan
	#41	Georg Schaeffler	$21.8 B	53	auto parts	Germany
	#42	Giovanni Ferrero	$21.3 B	53	Nutella, chocolates	Italy
	#43	Thomas Peterffy	$20.7 B	73	discount brokerage	United States
	#44	Len Blavatnik	$20.5 B	61	diversified	United States
	#45	Laurene Powell Jobs	$20.2 B	54	Apple, Disney	United States
	#46	Elon Musk	$20.2 B	47	Tesla Motors	United States
	#47	Paul Allen	$20.1 B	65	Microsoft, investments	United States
	#48	Vladimir Lisin	$20.1 B	62	steel, transport	Russia
	#49	James Simons	$20 B	80	hedge funds	United States
	#50	Stefan Quandt	$20 B	52	BMW	Germany
	#51	Theo Albrecht, Jr.	$19.6 B	67	Aldi, Trader Joe's	Germany
	#52	Joseph Safra	$19.6 B	79	banking	Brazil
	#53	Leonid Mikhelson	$19.6 B	62	gas, chemicals	Russia
	#54	Rupert Murdoch	$19.5 B	87	newspapers, TV network	United States
	#55	Lui Che Woo	$19.4 B	89	casinos	Hong Kong
	#56	Pallonji Mistry	$19.1 B	89	construction	Ireland
	#57	Carl Icahn	$19 B	82	investments	United States
	#58	Ray Dalio	$18.9 B	68	hedge funds	United States
	#59	Alexey Mordashov	$18.7 B	52	steel, investments	Russia
	#60	Harold Hamm	$18.4 B	72	oil & gas	United States
	#61	Henry Sy	$18.2 B	93	diversified	Philippines
	#62	Hinduja family	$18.2 B	-	diversified	United Kingdom
	#63	Vagit Alekperov	$18 B	67	oil	Russia
	#64	Gina Rinehart	$17.9 B	64	mining	Australia
	#65	Lee Kun-Hee	$17.7 B	76	Samsung	South Korea
	#66	He Xiangjian	$17.7 B	75	home appliances	China
	#67	Lakshmi Mittal	$17.4 B	68	steel	India
	#68	Gennady Timchenko	$17.3 B	65	oil, gas	Russia
	#69	Azim Premji	$17.3 B	72	software services	India
	#70	Wang Wei	$17.3 B	48	package delivery	China
	#71	Abigail Johnson	$16.6 B	56	money management	United States
	#72	Iris Fontbona	$16.5 B	75	mining	Chile
	#73	Joseph Lau	$16.4 B	66	real estate	Hong Kong
	#74	Donald Bren	$16.3 B	86	real estate	United States
	#75	Stefan Persson	$16.2 B	70	H&M	Sweden
	#76	Dustin Moskovitz	$16.1 B	34	Facebook	United States
	#77	Thomas & Raymond Kwok	$15.9 B	-	real estate	Hong Kong
	#78	Takemitsu Takizaki	$15.8 B	73	sensors	Japan
	#79	William Ding	$15.8 B	46	online games	China
	#80	Vladimir Potanin	$15.8 B	57	metals	Russia
	#81	Dieter Schwarz	$15.8 B	78	retail	Germany
	#82	German Larrea Mota Velasco	$15.8 B	64	mining	Mexico
	#83	Charlene de Carvalho-Heineken	$15.8 B	64	Heineken	Netherlands
	#84	James Ratcliffe	$15 B	65	chemicals	United Kingdom
	#85	Emmanuel Besnier	$14.9 B	47	cheese	France
	#86	David & Simon Reuben	$14.9 B	-	investments, real estate	United Kingdom
	#87	Charoen Sirivadhanabhakdi	$14.7 B	74	drinks, real estate	Thailand
	#88	Robin Li	$14.6 B	49	internet search	China
	#89	Robert Kuok	$14.5 B	94	palm oil, shipping, property	Malaysia
	#90	Zhang Zhidong	$14.5 B	46	internet media	China
	#91	R. Budi Hartono	$14.5 B	77	banking, tobacco	Indonesia
	#92	Eric Schmidt	$14.5 B	63	Google	United States
	#93	Petr Kellner	$14.4 B	54	banking	Czech Republic
	#94	Li Shufu	$14.3 B	55	automobiles	China
	#95	Lukas Walton	$14.3 B	31	Walmart	United States
	#96	Klaus-Michael Kuehne	$14.3 B	81	shipping	Germany
	#97	Hasso Plattner	$14.2 B	74	software	Germany
	#98	Philip Anschutz	$14.1 B	78	investments	United States
	#99	Pierre Castel & family	$14.1 B	91	wine	France
	#100	Mikhail Fridman	$14.1 B	54	oil, banking, telecom	Russia
	#101	Alain Wertheimer	$14 B	69	Chanel	France
	#101	Gerard Wertheimer	$14 B	67	Chanel	France
	#103	Shiv Nadar	$13.9 B	72	software services	India
	#104	Michael Hartono	$13.9 B	78	banking, tobacco	Indonesia
	#105	Leonard Lauder	$13.7 B	81	Estee Lauder	United States
	#106	Andrey Melnichenko	$13.6 B	46	coal, fertilizers	Russia
	#107	Marcel Herrmann Telles	$13.5 B	68	beer	Brazil
	#108	Dhanin Chearavanont	$13.5 B	79	diversified	Thailand
	#109	Viktor Vekselberg	$13.5 B	61	metals, energy	Russia
	#110	Stephen Schwarzman	$13.2 B	71	investments	United States
	#111	Udo & Harald Tschira	$13 B	-	software	Germany
	#112	Uday Kotak	$12.8 B	59	banking	India
	#113	Alisher Usmanov	$12.7 B	64	steel, telecom, investments	Russia
	#114	Hans Rausing	$12.5 B	92	packaging	Sweden
	#115	Radhakishan Damani	$12.5 B	63	investments, retail	India
	#116	Lei Jun	$12.4 B	48	smartphones	China
	#117	Reinhold Wuerth	$12.2 B	83	fasteners	Germany
	#118	Aliko Dangote	$12.2 B	61	cement, sugar, flour	Nigeria
	#119	Luis Carlos Sarmiento	$12 B	85	banking	Colombia
	#120	Andrew Beal	$12 B	65	banks, real estate	United States
	#121	Donald Newhouse	$11.9 B	88	media	United States
	#122	Peter Woo	$11.8 B	71	real estate	Hong Kong
	#123	Roman Abramovich	$11.8 B	51	steel, investments	Russia
	#124	Lee Man Tat	$11.6 B	88	Oyster sauce, real estate	Hong Kong
	#125	Eduardo Saverin	$11.6 B	36	Facebook	Brazil
	#126	Alexander Otto	$11.6 B	51	real estate	Germany
	#127	Steve Cohen	$11.4 B	62	hedge funds	United States
	#128	Carlos Alberto Sicupira	$11.4 B	70	beer	Brazil
	#129	Dilip Shanghvi	$11.4 B	62	pharmaceuticals	India
	#130	John Menard, Jr.	$11.3 B	78	home improvement stores	United States
	#131	Dietmar Hopp	$11.3 B	78	software	Germany
	#132	Heinz Hermann Thiele	$11.1 B	77	brakes	Germany
	#133	Pierre Omidyar	$11 B	51	eBay	United States
	#134	Stefano Pessina	$11 B	77	drugstores	Italy
	#135	David Tepper	$11 B	60	hedge funds	United States
	#136	Seo Jung-Jin	$10.8 B	60	biotech	South Korea
	#137	Charles Butt & family	$10.7 B	80	supermarkets	United States
	#138	Charles Ergen	$10.7 B	65	satellite TV	United States
	#139	Heinrich Deichmann & family	$10.6 B	55	footwear	Germany
	#140	Michael Otto	$10.5 B	75	retail, real estate	Germany
	#141	Joseph Tsai	$10.5 B	54	e-commerce	Canada
	#142	Robert & Philip Ng	$10.3 B	-	real estate	Singapore
	#143	James Goodnight	$10.2 B	75	software	United States
	#144	Gong Hongjia	$10.2 B	53	video surveillance	Hong Kong
	#145	Sun Piaoyang	$10.1 B	59	pharmaceuticals	China
	#146	Kumar Birla	$10.1 B	51	commodities	India
	#147	Harry Triguboff	$10.1 B	85	real estate	Australia
	#148	Thomas Frist, Jr.	$10 B	79	health care	United States
	#149	Ronald Perelman	$9.9 B	75	leveraged buyouts	United States
	#150	Walter P.J. Droege	$9.9 B	65	consulting	Germany
	#151	Alberto Bailleres Gonzalez	$9.9 B	86	mining	Mexico
	#152	Gordon Moore	$9.8 B	89	Intel	United States
	#153	Wang Wenyin	$9.8 B	50	mining, copper products	China
	#154	Liu Qiangdong	$9.7 B	43	e-commerce	China
	#155	Xu Shihui	$9.7 B	60	snacks, beverages	China
	#156	Graeme Hart	$9.6 B	63	investments	New Zealand
	#157	Blair Parry-Okeden	$9.6 B	68	media	United States
	#157	Jim Kennedy	$9.6 B	70	media	United States
	#159	Charles Schwab	$9.6 B	80	discount brokerage	United States
	#160	Jan Koum	$9.4 B	42	WhatsApp	United States
	#161	Galen Weston	$9.3 B	77	retail	Canada
	#162	Herbert Kohler, Jr.	$9.3 B	79	plumbing fixtures	United States
	#163	August von Finck	$9.2 B	88	investments	Germany
	#164	Mikhail Prokhorov	$9.2 B	53	investments	Russia
	#165	Carrie Perrodo	$9.2 B	67	oil	France
	#166	German Khan	$9.1 B	56	oil, banking, telecom	Russia
	#167	Eyal Ofer	$9.1 B	68	real estate, shipping	Israel
	#168	Zong Qinghou	$9.1 B	72	beverages	China
	#169	Ken Griffin	$9 B	49	hedge funds	United States
	#170	Micky Arison	$9 B	69	Carnival Cruises	United States
	#171	Daniel Tsai & family	$9 B	-	finance	Taiwan
	#172	Pang Kang	$8.9 B	62	soy sauce maker	China
	#173	Viktor Rashnikov	$8.9 B	69	steel	Russia
	#174	Carl Cook	$8.9 B	55	medical devices	United States
	#175	Yan Zhi	$8.8 B	45	real estate	China
	#176	David Duffield	$8.8 B	77	business software	United States
	#177	James Irving	$8.7 B	90	diversified	Canada
	#178	Giorgio Armani	$8.6 B	83	luxury goods	Italy
	#179	Ernesto Bertarelli	$8.5 B	52	biotech, investments	Switzerland
	#180	David Geffen	$8.4 B	75	movies, record labels	United States
	#181	John Doerr	$8.4 B	67	venture capital	United States
	#182	Gianluigi & Rafaela Aponte	$8.4 B	78	Shipping	Switzerland
	#183	Goh Cheng Liang	$8.4 B	91	paints	Singapore
	#184	Stanley Kroenke	$8.3 B	70	sports, real estate	United States
	#185	Hui Wing Mau	$8.3 B	68	real estate	Hong Kong
	#186	Melker Schorling	$8.3 B	71	investments	Sweden
	#187	George Soros	$8 B	87	hedge funds	United States
	#188	George Kaiser	$7.9 B	75	oil & gas, banking	United States
	#189	Michael Kadoorie	$7.9 B	76	hotels, energy	Hong Kong
	#190	Ma Jianrong	$7.8 B	54	textiles, apparel	China
	#191	Cyrus Poonawalla	$7.8 B	77	vaccines	India
	#192	Edward Johnson, III.	$7.8 B	88	money management	United States
	#193	Walter Kwok	$7.8 B	67	real estate	Hong Kong
	#194	Yao Zhenhua	$7.7 B	48	conglomerate	China
	#195	Nicky Oppenheimer	$7.7 B	73	diamonds	South Africa
	#196	John Malone	$7.6 B	77	cable television	United States
	#197	Loretta Robinson & family	$7.6 B	79	cable tv	Canada
	#198	Savitri Jindal	$7.6 B	68	steel	India
	#199	Jorn Rausing	$7.6 B	58	packaging	Sweden
	#200	David Green	$7.6 B	76	retail	United States
	#201	Wu Yajun	$7.6 B	54	real estate	China
	#202	Patrick Soon-Shiong	$7.6 B	65	pharmaceuticals	United States
	#203	Johann Graf	$7.6 B	71	gambling	Austria
	#204	Stephen Ross	$7.6 B	78	real estate	United States
	#205	Nusli Wadia	$7.5 B	74	consumer goods	India
	#206	Massimiliana Landini Aleotti	$7.5 B	75	pharmaceuticals	Italy
	#207	Terry Gou	$7.5 B	67	electronics	Taiwan
	#208	Leonid Fedun	$7.5 B	62	oil	Russia
	#209	Guo Guangchang	$7.5 B	51	conglomerate	China
	#210	Sunil Mittal	$7.4 B	60	telecom	India
	#211	Pauline MacMillan Keinath	$7.4 B	84	Cargill	United States
	#212	Tsai Eng-Meng	$7.4 B	61	food, beverages	Taiwan
	#213	John Fredriksen	$7.3 B	73	shipping	Cyprus
	#214	Iskander Makhmudov	$7.3 B	54	mining, metals, machinery	Russia
	#215	Charles Cadogan & family	$7.3 B	81	real estate	United Kingdom
	#216	Eli Broad	$7.3 B	85	investments	United States
	#217	Sandra Ortega Mera	$7.3 B	50	Zara	Spain
	#218	Frederik Paulsen	$7.2 B	67	health care	Sweden
	#219	Shahid Khan	$7.2 B	67	auto parts	United States
	#220	Gautam Adani	$7.2 B	56	commodities, ports	India
	#221	Pan Zhengmin	$7.1 B	48	electronics	China
	#222	Anders Holch Povlsen	$7.1 B	45	fashion retail	Denmark
	#223	Quek Leng Chan	$7.1 B	76	banking, property	Malaysia
	#224	Alexei Kuzmichev	$7.1 B	55	oil, banking, telecom	Russia
	#225	Sun Hongbin	$7 B	55	real estate	United States
	#226	Sri Prakash Lohia	$7 B	65	polyester	Indonesia
	#227	Silvio Berlusconi	$7 B	81	media	Italy
	#228	John A. Sobrato	$7 B	79	real estate	United States
	#229	Pham Nhat Vuong	$7 B	49	diversified	Vietnam
	#230	Andreas von Bechtolsheim	$6.9 B	62	Google	Germany
	#231	Hank & Doug Meijer	$6.9 B	-	supermarkets	United States
	#232	Ralph Lauren	$6.9 B	78	Ralph Lauren	United States
	#233	Jay Y. Lee	$6.9 B	50	Samsung	South Korea
	#234	Jim Pattison	$6.9 B	89	diversified	Canada
	#235	Eva Gonda de Rivera	$6.9 B	-	beverages	Mexico
	#236	Dmitry Rybolovlev	$6.8 B	51	fertilizer	Russia
	#237	Zhang Bangxin	$6.8 B	38	after-school tutoring	China
	#238	Willi & Isolde Liebherr	$6.8 B	-	Construction	Switzerland
	#239	Leon Black	$6.8 B	66	private equity	United States
	#240	Wu Shaoxun	$6.7 B	62	wine	China
	#241	Nassef Sawiris	$6.7 B	57	construction, chemicals	Egypt
	#242	Finn Rausing	$6.6 B	63	packaging	Sweden
	#242	Kirsten Rausing	$6.6 B	66	packaging	Sweden
	#244	Jiang Rensheng	$6.6 B	64	vaccine production	China
	#245	David Sun	$6.6 B	66	computer hardware	United States
	#245	John Tu	$6.6 B	76	computer hardware	United States
	#247	Johann Rupert	$6.6 B	68	luxury goods	South Africa
	#248	Odd Reitan	$6.6 B	66	retail, real estate	Norway
	#249	Christy Walton	$6.6 B	69	Walmart	United States
	#250	Acharya Balkrishna	$6.6 B	45	consumer goods	India
	#251	Augusto & Giorgio Perfetti	$6.6 B	-	candy	Italy
	#252	John Grayken	$6.6 B	62	private equity	Ireland
	#253	Brian Acton	$6.5 B	46	WhatsApp	United States
	#254	Kim Jung-Ju	$6.5 B	50	online games	South Korea
	#255	Michael Platt	$6.5 B	50	hedge funds	United Kingdom
	#256	Ricardo Salinas Pliego	$6.5 B	62	retail, media	Mexico
	#257	Wee Cho Yaw	$6.5 B	89	banking	Singapore
	#258	Daniel Gilbert	$6.4 B	56	Quicken Loans	United States
	#259	Richard Kinder	$6.4 B	73	pipelines	United States
	#260	Liu Yongxing	$6.4 B	70	diversified	China
	#261	Tom & Judy Love	$6.4 B	81	retail & gas stations	United States
	#262	Antonia Johnson	$6.4 B	74	diversified	Sweden
	#263	David Cheriton	$6.4 B	67	Google	Canada
	#264	Francis Choi	$6.4 B	70	real estate	Hong Kong
	#265	Suh Kyung-Bae	$6.3 B	55	cosmetics	South Korea
	#266	James Chambers	$6.3 B	61	media	United States
	#266	Katharine Rayner	$6.3 B	73	media	United States
	#266	Margaretta Taylor	$6.3 B	76	media	United States
	#269	Marijke Mars	$6.3 B	53	candy, pet food	United States
	#269	Pamela Mars	$6.3 B	57	candy, pet food	United States
	#269	Valerie Mars	$6.3 B	59	candy, pet food	United States
	#269	Victoria Mars	$6.3 B	61	candy, pet food	United States
	#273	Richard LeFrak	$6.3 B	72	real estate	United States
	#274	Ananda Krishnan	$6.2 B	80	telecoms, media, oil-services	Malaysia
	#275	John Paulson	$6.2 B	62	hedge funds	United States
	#276	Robert Kraft	$6.2 B	77	New England Patriots	United States
	#277	Dannine Avara	$6.2 B	54	pipelines	United States
	#278	Ian & Richard Livingstone	$6.2 B	-	real estate	United Kingdom
	#279	Marc Benioff	$6.2 B	53	business software	United States
	#280	Niels Peter Louis-Hansen	$6.2 B	70	medical devices	Denmark
	#281	David Shaw	$6.2 B	67	hedge funds	United States
	#282	Zhou Qunfei	$6.2 B	48	smartphone screens	Hong Kong
	#283	Jen-Hsun Huang	$6.1 B	55	semiconductors	United States
	#284	David & Frederick Barclay	$6.1 B	84	media, retail	United Kingdom
	#285	Akira Mori	$6.1 B	81	real estate	Japan
	#286	Whitney MacMillan	$6.1 B	88	Cargill	United States
	#287	Aloys Wobben	$6.1 B	66	wind turbines	Germany
	#288	Teh Hong Piow	$6.1 B	88	banking	Malaysia
	#289	Jim Davis	$6 B	75	New Balance	United States
	#290	Vikram Lal	$6 B	76	motorcycles	India
	#291	Maria Asuncion Aramburuzabala	$6 B	55	beer, investments	Mexico
	#292	Steven Rales	$6 B	67	manufacturing	United States
	#293	Edward Roski, Jr.	$6 B	79	real estate	United States
	#294	Xavier Niel	$6 B	50	internet, telecom	France
	#295	Israel Englander	$6 B	69	hedge funds	United States
	#296	Zhou Hongyi	$6 B	47	security software	China
	#297	Albert Frere	$6 B	92	investments	Belgium
	#298	Ann Walton Kroenke	$5.9 B	69	Walmart	United States
	#299	Dennis Washington	$5.9 B	83	construction, mining	United States
	#300	Frank Lowy	$5.9 B	87	shopping malls	Australia
	#301	Wolfgang Marguerre	$5.9 B	77	pharmaceuticals	Germany
	#302	Randa Williams	$5.9 B	56	pipelines	United States
	#303	Milane Frantz	$5.9 B	48	pipelines	United States
	#303	Scott Duncan	$5.9 B	35	pipelines	United States
	#305	Alexander Abramov	$5.8 B	59	steel, mining	Russia
	#306	Ludwig Merckle	$5.8 B	53	pharmaceuticals	Germany
	#307	Pierre Chen	$5.8 B	60	art, electronics	Taiwan
	#308	Zhang Jindong	$5.8 B	55	appliance retailer	China
	#309	George Roberts	$5.8 B	74	private equity	United States
	#310	Keiichiro Takahara	$5.8 B	87	diapers	Japan
	#311	Lu Zhiqiang	$5.8 B	65	real estate	China
	#312	Abdulla bin Ahmad Al Ghurair	$5.8 B	-	diversified	United Arab Emirates
	#313	Hansjoerg Wyss	$5.8 B	83	medical devices	Switzerland
	#314	Vincent Bollore	$5.8 B	66	investments	France
	#315	Stef Wertheimer	$5.8 B	91	metalworking tools	Israel
	#316	Bruno Schroder	$5.7 B	85	banking	United Kingdom
	#317	J. Christopher Reyes	$5.7 B	64	food distribution	United States
	#317	Jude Reyes	$5.7 B	62	food distribution	United States
	#319	Kei Hoi Pang	$5.7 B	52	real estate	China
	#320	Henry Kravis	$5.7 B	74	private equity	United States
	#321	Ivan Glasenberg	$5.7 B	61	mining	Switzerland
	#322	Robert Rich, Jr.	$5.7 B	77	frozen foods	United States
	#323	Charles Dolan	$5.7 B	91	cable television	United States
	#324	Lin Yu-Ling	$5.6 B	81	real estate	Taiwan
	#325	Yeung Kin-man	$5.6 B	54	electronics	Hong Kong
	#326	Suleiman Kerimov	$5.6 B	52	investments	Russia
	#327	Emanuele (Lino) Saputo	$5.6 B	81	cheese	Canada
	#328	Ronda Stryker	$5.6 B	64	medical equipment	United States
	#329	Les Wexner	$5.6 B	80	retail	United States
	#330	Robert Rowling	$5.6 B	64	investments	United States
	#331	Laurence Graff	$5.6 B	80	diamond jewelry	United Kingdom
	#332	David Filo	$5.6 B	52	Yahoo	United States
	#333	Benu Gopal Bangur	$5.6 B	87	cement	India
	#334	Jerry Jones	$5.6 B	75	Dallas Cowboys	United States
	#335	Reinhold Schmieding	$5.6 B	63	medical devices	United States
	#336	Rinat Akhmetov	$5.5 B	51	steel, coal	Ukraine
	#337	Jean-Michel Besnier	$5.5 B	51	cheese	France
	#337	Marie Besnier Beauvalot	$5.5 B	37	cheese	France
	#339	Gabe Newell	$5.5 B	55	videogames	United States
	#340	Shigenobu Nagamori	$5.5 B	73	motors	Japan
	#341	Maria Fernanda Amorim	$5.5 B	83	energy, investments	Portugal
	#342	Michael Herz	$5.5 B	74	coffee	Germany
	#342	Wolfgang Herz	$5.5 B	67	coffee	Germany
	#344	Jason Jiang	$5.5 B	45	advertising	China
	#345	David Siegel	$5.5 B	56	hedge funds	United States
	#345	John Overdeck	$5.5 B	48	hedge funds	United States
	#347	Martin Viessmann	$5.5 B	64	heating equipment	Germany
	#348	Maria-Elisabeth Schaeffler-Thumann	$5.5 B	76	auto parts	Germany
	#349	Lam Wai Ying	$5.4 B	-	smartphone screens	Hong Kong
	#350	Bernard Marcus	$5.4 B	89	Home Depot	United States
	#351	Paolo & Gianfelice Mario Rocca	$5.4 B	-	pipe manufacturing	Italy
	#352	James Dyson	$5.4 B	71	vacuums	United Kingdom
	#353	Pierre Bellon	$5.4 B	88	food services	France
	#354	Martha Ingram	$5.4 B	82	book distribution, transportation	United States
	#355	Lim Kok Thay	$5.4 B	66	casinos	Malaysia
	#356	Kushal Pal Singh	$5.4 B	86	real estate	India
	#357	Margarita Louis-Dreyfus	$5.3 B	56	commodities	Switzerland
	#358	Wang Wenxue	$5.3 B	51	real estate	China
	#359	Yao Liangsong	$5.3 B	53	furniture	China
	#360	George Lucas	$5.3 B	74	Star Wars	United States
	#361	Agnete Kirk Thinggaard	$5.3 B	-	Lego	Denmark
	#361	Kjeld Kirk Kristiansen	$5.3 B	70	Lego	Denmark
	#361	Sofie Kirk Kristiansen	$5.3 B	42	Lego	Denmark
	#361	Thomas Kirk Kristiansen	$5.3 B	-	Lego	Denmark
	#365	Dan Olsson	$5.3 B	71	diversified	Sweden
	#366	Ralph Dommermuth	$5.3 B	54	internet service provider	Germany
	#367	Robert Pera	$5.3 B	40	wireless networking gear	United States
	#368	Richard DeVos	$5.3 B	92	Amway	United States
	#369	John Sall	$5.3 B	70	software	United States
	#370	Tamara Gustavson	$5.3 B	56	self storage	United States
	#371	Anthony Pratt	$5.2 B	58	manufacturing	Australia
	#372	Bruce Kovner	$5.2 B	73	hedge funds	United States
	#373	Nancy Walton Laurie	$5.2 B	67	Walmart	United States
	#374	Ted Lerner	$5.2 B	92	real estate	United States
	#375	Pan Sutong	$5.2 B	55	real estate, finance	Hong Kong
	#376	Guenther Fielmann	$5.2 B	78	optometry	Germany
	#377	Karen Pritzker	$5.2 B	60	hotels, investments	United States
	#378	Frederick Smith	$5.2 B	73	FedEx	United States
	#379	Vivek Chaand Sehgal	$5.1 B	61	auto parts	Australia
	#380	Shari Arison	$5.1 B	60	Carnival Cruises	Israel
	#381	Gabriella Meister	$5.1 B	70	appliances	Germany
	#382	Kwee family	$5.1 B	-	Real Estate	Singapore
	#383	Richard Branson	$5.1 B	67	Virgin	United Kingdom
	#384	Zhang Shiping	$5.1 B	71	aluminum products	China
	#385	Friede Springer	$5.1 B	75	publishing	Germany
	#386	Chen Bang	$5.1 B	52	hospitals	China
	#387	Li Shuirong	$5.1 B	62	petrochemicals	China
	#388	Ray Lee Hunt	$5.1 B	75	oil, real estate	United States
	#389	Jeremy Jacobs, Sr.	$5.1 B	78	concessions	United States
	#390	Joe Lewis	$5.1 B	81	investments	United Kingdom
	#391	Qiu Guanghe	$5 B	66	fashion retail	China
	#392	Tse Ping	$5 B	66	pharmaceuticals	China
	#393	Bajaj brothers	$5 B	-	diversified	India
	#394	Lee Shin Cheng	$5 B	79	palm oil, property	Malaysia
	#395	Rahel Blocher	$5 B	42	chemicals	Switzerland
	#396	Magdalena Martullo-Blocher	$5 B	49	chemicals	Switzerland
	#397	Kjell Inge Rokke	$5 B	59	shipping, seafood	Norway
	#398	Andrew Currie	$5 B	62	chemicals	United Kingdom
	#398	John Reece	$5 B	61	chemicals	United Kingdom
	#400	Juan Francisco Beckmann Vidal	$5 B	78	tequila	Mexico
	#401	Sam Zell	$5 B	76	real estate, private equity	United States
	#402	Sumner Redstone	$5 B	95	media	United States
	#403	Charles Johnson	$5 B	85	money management	United States
	#404	Robert Bass	$5 B	70	oil, investments	United States
	#405	Law Kar Po	$5 B	70	real estate	Hong Kong
	#406	Wei Jianjun	$5 B	54	automobiles	China
	#407	Yasumitsu Shigeta	$4.9 B	53	mobile phone retailer	Japan
	#408	John Morris	$4.9 B	70	sporting goods retail	United States
	#409	Jeffrey Skoll	$4.9 B	53	eBay	United States
	#410	Elisabeth Mohn	$4.9 B	77	publishing	Germany
	#411	Nathan Kirsh	$4.9 B	86	retail, real estate	Swaziland
	#412	Jack Dorsey	$4.9 B	41	Twitter	United States
	#413	Andrei Kozitsyn	$4.9 B	58	metals	Russia
	#414	Zhou Jianping	$4.9 B	58	fashion retail	China
	#415	Vichai Srivaddhanaprabha	$4.9 B	60	duty-free	Thailand
	#416	Andrei Skoch	$4.9 B	52	steel	Russia
	#417	Diane Hendricks	$4.8 B	71	roofing	United States
	#418	Jack & Laura Dangermond	$4.8 B	72	mapping software	United States
	#419	Pyotr Aven	$4.8 B	63	oil, banking, telecom	Russia
	#420	Bubba Cathy	$4.8 B	64	Chick-fil-A	United States
	#420	Dan Cathy	$4.8 B	65	Chick-fil-A	United States
	#422	Daniel Ziff	$4.8 B	46	investments	United States
	#422	Dirk Ziff	$4.8 B	54	investments	United States
	#422	Robert Ziff	$4.8 B	51	investments	United States
	#425	Garrett Camp	$4.8 B	39	Uber	Canada
	#425	Travis Kalanick	$4.8 B	41	Uber	United States
	#427	Trevor Rees-Jones	$4.8 B	66	oil & gas	United States
	#428	Philip & Cristina Green	$4.8 B	66	fashion retail	United Kingdom
	#429	Mark Scheinberg	$4.8 B	44	online gambling	Canada
	#430	Wang Yusuo	$4.8 B	54	natural gas distribution	China
	#431	Yu Yong	$4.7 B	57	mining	China
	#432	Stewart and Lynda Resnick	$4.7 B	-	agriculture, water	United States
	#433	Gwendolyn Sontheim Meyer	$4.7 B	56	Cargill	United States
	#434	Alexandra Schoerghuber	$4.7 B	59	real estate	Germany
	#435	Bernard Broermann	$4.7 B	74	hospitals	Germany
	#436	Sheldon Solow	$4.7 B	89	real estate	United States
	#437	Denise Coates	$4.7 B	50	online gambling	United Kingdom
	#438	Frits Goldschmeding	$4.7 B	84	temp agency	Netherlands
	#439	Hiroshi Mikitani	$4.7 B	53	online retail	Japan
	#440	Clive Calder	$4.7 B	71	record label	United Kingdom
	#441	Pansy Ho	$4.7 B	55	casinos	Hong Kong
	#442	Stanley Druckenmiller	$4.7 B	65	hedge funds	United States
	#443	Gary Rollins	$4.6 B	73	pest control	United States
	#443	Randall Rollins	$4.6 B	86	pest control	United States
	#445	Chris Larsen	$4.6 B	58	cryptocurrency	United States
	#446	Fan Hongwei	$4.6 B	51	petrochemicals	China
	#447	Bidzina Ivanishvili	$4.6 B	62	investments	Georgia
	#448	Jeronimo Arango	$4.6 B	92	retail	Mexico
	#449	Cai Kui	$4.6 B	55	real estate	China
	#450	Martin & Olivier Bouygues	$4.6 B	-	construction, media	France
	#451	Rocco Commisso	$4.6 B	68	telecom	United States
	#452	Rahul Bajaj	$4.6 B	80	motorcycles	India
	#453	Ji Changqun	$4.5 B	50	real estate	China
	#454	Mike Adenuga	$4.5 B	65	telecom, oil	Nigeria
	#455	Theo Mueller	$4.5 B	78	dairy	Germany
	#456	Subhash Chandra	$4.5 B	67	media	India
	#457	Cao Longxiang	$4.5 B	60	pharmaceuticals	China
	#458	Mikhail Gutseriev	$4.5 B	60	oil, real estate	Russia
	#459	Paul Tudor Jones, II.	$4.5 B	63	hedge funds	United States
	#460	Liang Wengen	$4.5 B	61	construction equipment	China
	#461	Sergei Popov	$4.5 B	46	banking	Russia
	#462	Bertil Hult	$4.5 B	77	education	Sweden
	#463	Peter Hargreaves	$4.5 B	71	financial services	United Kingdom
	#464	Jean-Pierre Cayard	$4.5 B	75	spirits	France
	#465	Leonard Stern	$4.5 B	80	real estate	United States
	#466	Chan Laiwa	$4.5 B	77	real estate	China
	#467	Johan Johannson	$4.5 B	51	grocery stores	Norway
	#468	Juan Roig	$4.5 B	68	supermarkets	Spain
	#469	Richard Li	$4.4 B	51	telecom	Hong Kong
	#470	Lin Xiucheng	$4.4 B	62	electronics	China
	#471	Mike Cannon-Brookes	$4.4 B	38	software	Australia
	#471	Scott Farquhar	$4.4 B	38	software	Australia
	#473	Dona Bertarelli	$4.4 B	50	biotech	Switzerland
	#474	Stephen Bisciotti	$4.4 B	58	staffing, Baltimore Ravens	United States
	#475	Robert Smith	$4.4 B	55	private equity	United States
	#476	Andres Santo Domingo	$4.4 B	40	beer	United States
	#477	Alejandro Santo Domingo	$4.4 B	41	beer	United States
	#478	Russ Weiner	$4.4 B	48	energy drinks	United States
	#479	Michael Moritz	$4.4 B	63	venture capital	United States
	#480	Patrick Lee	$4.4 B	76	paper	Hong Kong
	#481	Tilman Fertitta	$4.4 B	61	Houston Rockets, entertainment	United States
	#482	Pankaj Patel	$4.4 B	65	pharmaceuticals	India
	#483	Luo Liguo	$4.4 B	62	chemicals	China
	#484	Denis O'Brien	$4.4 B	60	telecom	Ireland
	#485	Archie Aldis Emmerson	$4.4 B	89	timberland, lumber mills	United States
	#486	Thomas Schmidheiny	$4.4 B	72	cement	Switzerland
	#487	M.A. Yusuff Ali	$4.3 B	62	retail	India
	#488	Terrence Pegula	$4.3 B	67	natural gas	United States
	#489	Robert Miller	$4.3 B	85	retail	United Kingdom
	#490	Ajay Piramal	$4.3 B	62	pharmaceuticals	India
	#491	Kelcy Warren	$4.3 B	62	pipelines	United States
	#492	Jeffery Hildebrand	$4.3 B	59	oil	United States
	#493	Antti Herlin	$4.3 B	61	elevators, escalators	Finland
	#494	Arthur Blank	$4.3 B	75	Home Depot	United States
	#495	Reed Hastings	$4.3 B	57	Netflix	United States
	#496	Austen Cargill, II.	$4.2 B	67	Cargill	United States
	#496	James Cargill, II.	$4.2 B	69	Cargill	United States
	#496	Marianne Liebmann	$4.2 B	64	Cargill	United States
	#499	Juan Carlos Escotet	$4.2 B	58	banking	Venezuela
	#500	H. Ross Perot, Sr.	$4.2 B	88	computer services, real estate	United States
	#501	Richard Schulze	$4.2 B	77	Best Buy	United States
	#502	Arthur Irving	$4.2 B	88	oil	Canada
	#503	Igor Olenicoff	$4.2 B	75	real estate	United States
	#504	Paul Gauselmann	$4.2 B	83	gambling	Germany
	#505	Lai Meisong	$4.2 B	47	package delivery	China
	#506	James Jannard	$4.2 B	69	sunglasses	United States
	#507	Cheng Cheung Ling	$4.2 B	54	pharmaceuticals	China
	#508	Juergen Blickle	$4.2 B	71	auto parts	Germany
	#509	Chu Mang Yee	$4.2 B	58	real estate	China
	#510	Andrei Guriev	$4.2 B	58	fertilizers	Russia
	#511	Matthias Reimann-Andersen	$4.2 B	53	consumer goods	Germany
	#511	Renate Reimann-Haas	$4.2 B	66	consumer goods	Germany
	#511	Stefan Reimann-Andersen	$4.2 B	54	consumer goods	Germany
	#511	Wolfgang Reimann	$4.2 B	65	consumer goods	Germany
	#515	Walter Scott, Jr.	$4.2 B	87	utilities, telecom	United States
	#516	Julio Ponce Lerou	$4.2 B	72	fertilizer	Chile
	#517	Majid Al Futtaim	$4.2 B	-	real estate, retail	United Arab Emirates
	#518	Clemmie Spangler, Jr.	$4.2 B	86	investments	United States
	#519	B.R. Shetty	$4.2 B	76	healthcare	India
	#520	Thomas Pritzker	$4.2 B	68	hotels, investments	United States
	#521	Giuseppe De'Longhi	$4.2 B	79	coffee makers	Italy
	#522	Rupert Johnson, Jr.	$4.2 B	77	money management	United States
	#523	Che Jianxing	$4.1 B	51	furniture retailing	China
	#524	Akio Nitori	$4.1 B	74	home furnishings	Japan
	#525	Murat Ulker	$4.1 B	59	food	Turkey
	#526	Isaac Perlmutter	$4.1 B	75	Marvel comics	United States
	#527	Wang Chuanfu	$4.1 B	52	batteries, automobiles	China
	#528	Fredrik Lundberg	$4.1 B	66	real estate, investments	Sweden
	#529	Julian Robertson, Jr.	$4.1 B	86	hedge funds	United States
	#530	Kwon Hyuk-Bin	$4.1 B	44	online games	South Korea
	#531	Chung Mong-Koo	$4.1 B	80	motor vehicles	South Korea
	#532	Ernest Garcia, II.	$4.1 B	61	used cars	United States
	#533	Dan Friedkin	$4.1 B	53	Toyota dealerships	United States
	#534	Naguib Sawiris	$4.1 B	64	telecom	Egypt
	#535	Miguel Fluxa Rossello	$4.1 B	79	hotels	Spain
	#536	Ji Qi	$4.1 B	51	hotels, motels	China
	#537	John Gokongwei, Jr.	$4.1 B	91	food and beverage	Philippines
	#538	Cai Dongchen	$4.1 B	65	pharmaceuticals	China
	#539	Melissa Ma	$4.1 B	48	internet search	China
	#540	Dagmar Dolby	$4.1 B	77	Dolby Laboratories	United States
	#541	Wang Xing	$4.1 B	45	e-commerce	China
	#542	Chey Tae-Won	$4.1 B	57	IT, telecom	South Korea
	#543	Liu Yonghao	$4.1 B	66	agribusiness	China
	#544	Pedro Moreira Salles	$4.1 B	58	banking, minerals	Brazil
	#545	James Packer	$4.1 B	50	casinos	Australia
	#546	Ronald Lauder	$4 B	74	Estee Lauder	United States
	#547	Ye Chenghai	$4 B	74	pharmaceuticals	Hong Kong
	#548	Nie Tengyun	$4 B	42	logistics	China
	#549	Kalanithi Maran	$4 B	52	media	India
	#550	Kuldip Singh & Gurbachan Singh Dhingra	$4 B	-	paints	India
	#551	Andrej Babis	$4 B	63	agriculture	Czech Republic
	#552	Joao Moreira Salles	$4 B	56	banking, minerals	Brazil
	#553	Fernando Roberto Moreira Salles	$4 B	72	banking, minerals	Brazil
	#553	Walther Moreira Salles Junior	$4 B	62	banking, minerals	Brazil
	#555	Martin Ebner	$4 B	72	investments	Switzerland
	#556	Ben Ashkenazy	$4 B	48	real estate	United States
	#556	Traudl Engelhorn	$4 B	91	pharmaceuticals, medical equipment	Germany
	#556	Zhang Yiming	$4 B	34	software	China
	#559	Sumet Jiaravanon	$4 B	83	diversified	Thailand
	#560	Nick Caporella	$4 B	82	beverages	United States
	#561	Yusaku Maezawa	$4 B	42	online retail	Japan
	#562	Anthony Bamford	$4 B	72	construction equipment	United Kingdom
	#563	John Gandel	$4 B	83	shopping malls	Australia
	#564	Jeff Sutton	$4 B	58	real estate	United States
	#565	Issad Rebrab	$4 B	74	food	Algeria
	#566	Kapil & Rahul Bhatia	$4 B	-	airlines	India
	#567	Tom Gores	$3.9 B	53	private equity	United States
	#568	Rick Caruso	$3.9 B	59	real estate	United States
	#569	Jerry Speyer	$3.9 B	78	real estate	United States
	#570	Samuel Yin	$3.9 B	67	diversified	Taiwan
	#571	Douglas Leone	$3.9 B	61	venture capital	United States
	#572	Roger Wang	$3.9 B	69	retail	United States
	#573	Pawan Munjal	$3.9 B	64	motorcycles	India
	#574	Xu Chuanhua	$3.9 B	83	chemicals, logistics	China
	#575	Martin Lorentzon	$3.9 B	49	Spotify	Sweden
	#576	Steven Udvar-Hazy	$3.9 B	72	aircraft leasing	United States
	#577	Jaran Chiaravanont	$3.9 B	88	diversified	Thailand
	#578	Henry Samueli	$3.9 B	63	semiconductors	United States
	#579	Montri Jiaravanont	$3.9 B	87	diversified	Thailand
	#580	Samuel Tak Lee	$3.9 B	79	real estate	Hong Kong
	#581	Scott Cook	$3.9 B	65	software	United States
	#582	Ursula Bechtolsheimer-Kipp	$3.9 B	-	retail	Germany
	#583	Otto Philipp Braun	$3.9 B	40	medical technology	Germany
	#584	Masatoshi Ito	$3.9 B	94	retail	Japan
	#585	Ira Rennert	$3.8 B	84	investments	United States
	#586	Angela Leong	$3.8 B	57	casinos	Hong Kong
	#587	Chairul Tanjung	$3.8 B	56	diversified	Indonesia
	#588	Horst Paulmann	$3.8 B	83	retail	Chile
	#589	Carl Bennet	$3.8 B	66	investments	Sweden
	#590	Axel Oberwelland	$3.8 B	51	candy	Germany
	#591	Brian Chesky	$3.8 B	36	Airbnb	United States
	#591	Joe Gebbia	$3.8 B	36	Airbnb	United States
	#591	Nathan Blecharczyk	$3.8 B	35	Airbnb	United States
	#594	Zhang Xuexin	$3.8 B	71	aluminum	China
	#595	Rainer Blickle	$3.8 B	70	auto parts	Germany
	#596	Jeff Greene	$3.8 B	63	real estate, investments	United States
	#597	Karsanbhai Patel	$3.8 B	74	consumer goods	India
	#598	Dominika & Sebastian Kulczyk	$3.8 B	-	diversified	Poland
	#599	Li Ge	$3.8 B	51	biotech	China
	#600	Michel Leclercq	$3.8 B	79	sporting goods	France
	#601	Andrew Forrest	$3.8 B	56	mining	Australia
	#602	Fu Liquan	$3.8 B	50	surveillance equipment	China
	#603	Robert McNair	$3.8 B	81	energy, sports	United States
	#604	Ravi Pillai	$3.8 B	64	construction	India
	#605	Daniela Herz	$3.8 B	64	coffee	Germany
	#605	Guenter Herz	$3.8 B	77	coffee	Germany
	#607	Mitchell Rales	$3.8 B	61	manufacturing, investments	United States
	#608	Katharina Otto-Bernstein	$3.8 B	-	real estate	Germany
	#609	John Brown	$3.7 B	83	medical equipment	United States
	#610	Ashwin Dani	$3.7 B	75	paints	India
	#611	Mark Cuban	$3.7 B	59	online media	United States
	#612	Shen Yuxing	$3.7 B	59	real estate	China
	#613	Michael Milken	$3.7 B	72	investments	United States
	#614	Michael Ashley	$3.7 B	53	sports retailing	United Kingdom
	#615	Pat Stryker	$3.7 B	62	medical equipment	United States
	#616	Christoph Zeller	$3.7 B	61	dental implants	Liechtenstein
	#617	Manuel Villar	$3.7 B	68	real estate	Philippines
	#618	Anne Beaufour	$3.7 B	54	pharmaceuticals	France
	#618	Henri Beaufour	$3.7 B	53	pharmaceuticals	France
	#620	Arnon Milchan	$3.7 B	73	movie making	Israel
	#621	Yuri Milner	$3.7 B	56	tech investments	Russia
	#622	Patrick Drahi	$3.7 B	54	telecom	France
	#623	Renzo Rosso	$3.7 B	62	fashion	Italy
	#624	Patrizio Bertelli	$3.7 B	72	luxury goods	Italy
	#625	Miuccia Prada	$3.7 B	69	luxury goods	Italy
	#626	Hubert Burda	$3.7 B	78	publishing	Germany
	#627	Ken Fisher	$3.7 B	67	money management	United States
	#628	Li Wa	$3.7 B	52	real estate	Hong Kong
	#629	Andreas Halvorsen	$3.7 B	57	hedge funds	Norway
	#630	Jaime Gilinski Bacal	$3.6 B	60	banking	Colombia
	#631	Sergei Galitsky	$3.6 B	50	retail	Russia
	#632	Jimmy Haslam	$3.6 B	64	gas stations, retail	United States
	#633	Chen Dongsheng	$3.6 B	60	insurance	China
	#634	Joshua Harris	$3.6 B	53	private equity	United States
	#635	Steven Spielberg	$3.6 B	71	Movies	United States
	#636	Clifford Asness	$3.6 B	51	Investment Management	United States
	#637	Sudhir & Samir Mehta	$3.6 B	-	diversified	India
	#638	Clemens Toennies	$3.6 B	62	meat processing	Germany
	#639	Viatcheslav Kantor	$3.6 B	64	fertilizer, real estate	Russia
	#640	Zhang Jin	$3.6 B	46	diversified	China
	#641	Chip Wilson	$3.6 B	61	Lululemon	Canada
	#642	Marc Ladreit de Lacharriere	$3.6 B	77	finance	France
	#643	Peter Gilgan	$3.6 B	67	homebuilding	Canada
	#644	Bernard Saul, II.	$3.6 B	86	banking, real estate	United States
	#645	Antonio Del Valle Ruiz	$3.6 B	79	chemicals	Mexico
	#646	Sid Bass	$3.6 B	76	oil, investments	United States
	#647	Yitzhak Tshuva	$3.6 B	70	real estate	Israel
	#648	Kerry Stokes	$3.6 B	77	construction equipment, media	Australia
	#649	Andreas Struengmann	$3.6 B	68	pharmaceuticals	Germany
	#649	Thomas Struengmann	$3.6 B	68	pharmaceuticals	Germany
	#651	Helen Johnson-Leipold	$3.5 B	61	cleaning products	United States
	#651	S. Curtis Johnson	$3.5 B	63	cleaning products	United States
	#651	Winifred Johnson-Marquart	$3.5 B	59	cleaning products	United States
	#654	Barry Lam	$3.5 B	69	electronics	Taiwan
	#655	Enrique Razon, Jr.	$3.5 B	58	ports	Philippines
	#656	Edward Johnson, IV.	$3.5 B	53	money management	United States
	#656	Elizabeth Johnson	$3.5 B	55	money management	United States
	#658	Donald Sterling	$3.5 B	84	real estate	United States
	#659	Ronald McAulay	$3.5 B	82	energy	Hong Kong
	#660	Zeng Fangqin	$3.5 B	52	smartphone components	China
	#661	Carlos Rodriguez-Pastor	$3.5 B	59	finance	Peru
	#662	Chen Lip Keong	$3.5 B	71	casinos, property, energy	Malaysia
	#663	Kiran Mazumdar-Shaw	$3.5 B	65	biotech	India
	#664	H. Fisk Johnson	$3.5 B	60	cleaning products	United States
	#665	Frank VanderSloot	$3.5 B	69	nutrition and wellness products	United States
	#666	Rudolf Maag	$3.5 B	72	medical devices	Switzerland
	#667	Masahiro Miki	$3.5 B	62	shoes	Japan
	#668	Gustaf Douglas	$3.5 B	80	investments	Sweden
	#669	Judy Faulkner	$3.5 B	74	health IT	United States
	#670	Edwin Leong	$3.5 B	66	real estate	Hong Kong
	#671	Michael Pieper	$3.5 B	72	kitchen appliances	Switzerland
	#672	Henry Nicholas, III.	$3.5 B	58	semiconductors	United States
	#673	Lucio Tan	$3.5 B	83	diversified	Philippines
	#674	Fang Wei	$3.5 B	44	steel	China
	#675	Xu Jingren	$3.5 B	73	pharmaceuticals	China
	#676	Min Kao	$3.5 B	69	navigation equipment	United States
	#677	Wang Zhenhua	$3.5 B	56	real estate	China
	#678	Lars Larsen	$3.5 B	69	retail	Denmark
	#679	Anthony Pritzker	$3.5 B	57	hotels, investments	United States
	#679	Jay Robert (J.B.) Pritzker	$3.5 B	53	hotels, investments	United States
	#681	Maren Otto	$3.5 B	-	retail, real estate	Germany
	#682	Anil Agarwal	$3.5 B	64	mining, metals	India
	#683	Friedhelm Loh	$3.4 B	71	manufacturing	Germany
	#684	Kenneth Langone	$3.4 B	82	investments	United States
	#685	Nicolas Puech	$3.4 B	75	Hermes	France
	#686	Du Weimin	$3.4 B	54	vaccines	China
	#687	Jiang Weiping	$3.4 B	63	chemicals	China
	#688	Oleg Deripaska	$3.4 B	50	aluminum, utilities	Russia
	#689	Joe Mansueto	$3.4 B	61	investment research	United States
	#690	Rita Tong Liu	$3.4 B	70	real estate	Hong Kong
	#691	Tahir	$3.4 B	66	diversified	Indonesia
	#692	Tom Golisano	$3.4 B	76	payroll services	United States
	#693	Rafael Del Pino y Calvo-Sotelo	$3.4 B	59	construction	Spain
	#694	George Lindemann	$3.4 B	82	investments	United States
	#695	Yvonne Bauer	$3.4 B	41	media	Germany
	#696	Carlo Benetton	$3.4 B	74	fashion retail, investments	Italy
	#696	Gilberto Benetton	$3.4 B	77	fashion retail, investments	Italy
	#696	Giuliana Benetton	$3.4 B	81	fashion retail, investments	Italy
	#699	Luciano Benetton	$3.4 B	83	fashion retail, investments	Italy
	#700	Peter Kellogg	$3.4 B	75	investments	United States
	#701	Micky Jagtiani	$3.4 B	66	retail	India
	#702	Igor Altushkin	$3.4 B	47	metals	Russia
	#703	Shaul Shani	$3.4 B	63	telecom	Israel
	#704	Charles Cohen	$3.3 B	66	real estate	United States
	#705	Prasert Prasarttong-Osoth	$3.3 B	85	hospitals	Thailand
	#706	Shashi & Ravi Ruia	$3.3 B	-	diversified	India
	#707	Harry Stine	$3.3 B	76	agriculture	United States
	#708	Ding Shizhong	$3.3 B	47	sports apparel	China
	#709	Bernard Ecclestone	$3.3 B	87	Formula One	United Kingdom
	#710	Reid Hoffman	$3.3 B	50	LinkedIn	United States
	#711	Marc Rowan	$3.3 B	55	private equity	United States
	#712	Dmitry Kamenshchik	$3.3 B	50	airport	Russia
	#713	Neil Bluhm	$3.3 B	80	real estate	United States
	#714	Barry Diller	$3.3 B	76	online media	United States
	#715	Suhail Bahwan	$3.3 B	79	diversified	Oman
	#716	Abdulla Al Futtaim	$3.3 B	-	auto dealers, investments	United Arab Emirates
	#717	Alexander Skorobogatko	$3.3 B	50	real estate, airport	Russia
	#718	Alexander Ponomarenko	$3.3 B	53	real estate, airport	Russia
	#719	Meg Whitman	$3.3 B	61	eBay	United States
	#720	Teddy Sagi	$3.3 B	46	gambling software	Israel
	#721	Jeff Rothschild	$3.3 B	63	Facebook	United States
	#722	Liu Zhongtian	$3.3 B	54	aluminum products	China
	#723	John Arnold	$3.3 B	44	hedge funds	United States
	#724	John Paul DeJoria	$3.3 B	74	hair products, tequila	United States
	#725	Lindsay Fox	$3.3 B	81	logistics, real estate	Australia
	#726	Arne Wilhelmsen	$3.3 B	88	cruise ships	Norway
	#727	Jon Stryker	$3.3 B	60	medical equipment	United States
	#728	Riley Bechtel	$3.3 B	66	engineering, construction	United States
	#728	Stephen Bechtel, Jr.	$3.3 B	93	engineering, construction	United States
	#730	Yakir Gabay	$3.3 B	52	real estate	Cyprus
	#731	Andrew & Peggy Cherng	$3.3 B	-	restaurants	United States
	#732	Zhang Xin	$3.3 B	52	real estate	China
	#733	Heidi Horten	$3.3 B	77	retail	Austria
	#734	Qin Yinglin	$3.2 B	53	pig breeding	China
	#735	Rodger Riney	$3.2 B	72	discount brokerage	United States
	#736	Alain Merieux	$3.2 B	80	pharmaceuticals	France
	#737	Amos Hostetter, Jr.	$3.2 B	81	cable television	United States
	#738	Erman Ilicak	$3.2 B	50	construction	Turkey
	#739	Ding Shijia	$3.2 B	54	sportswear	China
	#740	Tony Tan Caktiong	$3.2 B	65	food	Philippines
	#741	Yu Huijiao	$3.2 B	52	package delivery	China
	#742	Richard Sands	$3.2 B	67	Food & Beverage	United States
	#743	Jim Breyer	$3.2 B	56	venture capital	United States
	#744	Frank Wang	$3.2 B	37	drones	China
	#744	Leon G. Cooperman	$3.2 B	75	hedge funds	United States
	#744	Lynn Schusterman	$3.2 B	79	oil & gas, investments	United States
	#747	Martin Haefner	$3.2 B	64	software, investments	Switzerland
	#748	Mark Walter	$3.2 B	58	finance	United States
	#749	Huang Rulun	$3.2 B	66	real estate	China
	#750	Ke Zunhong	$3.2 B	64	pharmaceuticals	China
	#751	Sameer Gehlaut	$3.2 B	44	finance	India
	#752	Daniel Och	$3.2 B	57	hedge funds	United States
	#753	Herbert Simon	$3.2 B	83	real estate	United States
	#754	Robert Sands	$3.2 B	60	Food & Beverage	United States
	#755	Vladimir Kim	$3.2 B	57	mining	Kazakhstan
	#756	Daniel Loeb	$3.2 B	56	hedge funds	United States
	#757	Drew Houston	$3.1 B	35	file hosting service	United States
	#758	Haim Saban	$3.1 B	73	TV network, investments	United States
	#759	Johnelle Hunt	$3.1 B	86	trucking	United States
	#760	Hans Peter Wild	$3.1 B	77	flavorings	Switzerland
	#761	Do Won & Jin Sook Chang	$3.1 B	62	fashion retail	United States
	#762	Jane Goldman	$3.1 B	62	real estate	United States
	#763	Daniel Tsai	$3.1 B	62	finance	Taiwan
	#764	Richard Tsai	$3.1 B	61	finance	Taiwan
	#765	Alain Bouchard	$3.1 B	69	retail	Canada
	#766	Alexander Svetakov	$3.1 B	50	real estate	Russia
	#767	Robert Toennies	$3.1 B	40	meat processing	Germany
	#768	Alvaro Saieh Bendeck	$3.1 B	68	banking	Chile
	#769	Jim Davis	$3.1 B	58	staffing & recruiting	United States
	#770	Amy Goldman Fowler	$3.1 B	64	real estate	United States
	#771	John Catsimatidis	$3.1 B	69	oil, real estate	United States
	#772	Sarath Ratanavadi	$3.1 B	52	energy	Thailand
	#773	Diane Kemper	$3.1 B	72	real estate	United States
	#774	Samvel Karapetyan	$3.1 B	52	real estate	Russia
	#775	Mary Alice Dorrance Malone	$3.1 B	68	Campbell Soup	United States
	#776	Mark Shoen	$3.1 B	67	U-Haul	United States
	#777	Allan Goldman	$3.1 B	75	real estate	United States
	#778	Hans Georg Naeder	$3.1 B	56	prosthetics	Germany
	#779	Karel Komarek	$3.1 B	49	lotteries	Czech Republic
	#780	Donald Trump	$3.1 B	72	television, real estate	United States
	#781	Wu Zhigang	$3.1 B	83	bakery chain	China
	#782	Randal Kirk	$3.1 B	64	pharmaceuticals	United States
	#783	Jean (Gigi) Pritzker	$3.1 B	56	hotels, investments	United States
	#784	Timur Kulibaev	$3.1 B	51	banking	Kazakhstan
	#785	Dinara Kulibaeva	$3.1 B	50	banking	Kazakhstan
	#786	Zhang Li	$3.1 B	65	real estate	China
	#787	Romesh T. Wadhwani	$3.1 B	70	software	United States
	#788	John Middleton	$3 B	63	tobacco	United States
	#789	Huang Shilin	$3 B	51	storage batteries	China
	#790	Otto Happel	$3 B	70	engineering	Germany
	#791	Michal Solowow	$3 B	55	investments	Poland
	#792	Krit Ratanarak	$3 B	72	media, real estate	Thailand
	#793	Piero Ferrari	$3 B	73	automobiles	Italy
	#794	Oprah Winfrey	$3 B	64	TV shows	United States
	#795	Bobby Murphy	$3 B	29	Snapchat	United States
	#796	Valentin Gapontsev	$3 B	79	lasers	United States
	#797	Gabriele Volkmann	$3 B	-	auto parts	Germany
	#798	Phillip Frost	$3 B	81	pharmaceuticals	United States
	#799	Luo Jye	$3 B	92	tires	Taiwan
	#800	David Rubenstein	$3 B	68	private equity	United States
	#801	Christopher Hohn	$3 B	51	Hedge funds	United Kingdom
	#802	Steve Wynn	$3 B	76	casinos, hotels	United States
	#803	Tung Chee Chen	$3 B	76	shipping	Hong Kong
	#804	Luis Frias	$3 B	55	mobile payments	Brazil
	#805	Bang Jun-Hyuk	$3 B	50	online gaming	South Korea
	#806	Jorge Perez	$3 B	68	real estate	United States
	#807	William Conway, Jr.	$3 B	68	private equity	United States
	#808	Don Vultaggio	$3 B	66	AriZona Beverages	United States
	#809	Daryl Katz	$3 B	56	pharmacies	Canada
	#810	Daniel D'Aniello	$3 B	71	private equity	United States
	#811	Evan Spiegel	$3 B	28	Snapchat	United States
	#812	James Leprino	$3 B	80	cheese	United States
	#813	Daniel Ek	$3 B	35	Spotify	Sweden
	#814	Feng Hailiang	$3 B	57	copper, education	China
	#815	Simon Xie	$3 B	48	online payment service	China
	#816	Rajan Raheja	$3 B	64	diversified	India
	#817	Gustavo Denegri	$3 B	82	biotech	Italy
	#818	Kurt Krieger	$3 B	70	furniture retailing	Germany
	#819	Michael Rubin	$3 B	45	online retail	United States
	#820	Alejandro Bulgheroni	$3 B	73	oil & gas	Argentina
	#821	Stephen Mandel, Jr.	$3 B	62	hedge funds	United States
	#822	Sun Guangxin	$2.9 B	55	diversified	China
	#823	Rishad Naoroji	$2.9 B	66	consumer goods	India
	#824	Adi Godrej	$2.9 B	76	consumer goods	India
	#824	Jamshyd Godrej	$2.9 B	69	consumer goods	India
	#824	Nadir Godrej	$2.9 B	67	consumer goods	India
	#824	Smita Crishna-Godrej	$2.9 B	67	consumer goods	India
	#828	Vincent McMahon	$2.9 B	72	wrestling	United States
	#829	Tom Morris	$2.9 B	63	retail	United Kingdom
	#830	Cheng Xue	$2.9 B	48	soy sauce	China
	#831	Edward DeBartolo, Jr.	$2.9 B	71	shopping centers	United States
	#832	Aloke Lohia	$2.9 B	59	petrochemicals	India
	#833	Thomas Straumann	$2.9 B	54	dental implants	Switzerland
	#834	Thomas Secunda	$2.9 B	64	Bloomberg LP	United States
	#835	Gerald Ford	$2.9 B	73	banking	United States
	#836	George Ty	$2.9 B	85	banking	Philippines
	#837	Baba Kalyani	$2.9 B	69	engineering	India
	#838	Chuck Bundrant	$2.9 B	76	fishing	United States
	#839	Idan Ofer	$2.9 B	62	drilling, shipping	Israel
	#840	Luca Garavoglia	$2.9 B	49	spirits	Italy
	#841	Huang Shih Tsai	$2.9 B	67	real estate	Hong Kong
	#842	Saeed Bin Butti Al Qebaisi	$2.9 B	-	hospitals, investments	United Arab Emirates
	#843	B. Wayne Hughes	$2.9 B	84	self storage	United States
	#844	Thomas Siebel	$2.9 B	65	business software	United States
	#845	Mortimer Zuckerman	$2.9 B	81	real estate, media	United States
	#846	Paul Singer	$2.8 B	73	hedge funds	United States
	#847	Jay Paul	$2.8 B	71	real estate	United States
	#848	Manuel Lao Hernandez	$2.8 B	74	gambling	Spain
	#849	Jason Chang	$2.8 B	74	electronics	Singapore
	#850	Georg Nemetschek	$2.8 B	84	software	Germany
	#851	Mochtar Riady	$2.8 B	89	diversified	Indonesia
	#852	Rakesh Jhunjhunwala	$2.8 B	58	investments	India
	#853	Radovan Vitek	$2.8 B	47	real estate	Czech Republic
	#854	Hussain Sajwani	$2.8 B	65	real estate	United Arab Emirates
	#855	Charles Simonyi	$2.8 B	69	Microsoft	United States
	#856	Li Gaiteng	$2.8 B	46	hair dryers	China
	#857	Sergio Mantegazza	$2.8 B	90	travel	Switzerland
	#858	God Nisanov	$2.8 B	46	real estate	Russia
	#858	Zarakh Iliev	$2.8 B	51	real estate	Russia
	#860	Joseph Grendys	$2.8 B	56	poultry processing	United States
	#861	Alicia Koplowitz	$2.8 B	64	construction, investments	Spain
	#862	Gu Yuhua	$2.8 B	68	furniture	China
	#863	Vanich Chaiyawan	$2.8 B	86	insurance, beverages	Thailand
	#864	Penny Pritzker	$2.8 B	59	hotels, investments	United States
	#865	Liang Xinjun	$2.8 B	50	conglomerate	China
	#866	Sebastian Piñera	$2.8 B	68	investments	Chile
	#867	Georg Stumpf	$2.8 B	45	real estate, construction	Austria
	#868	Vinod Khosla	$2.8 B	63	venture capital	United States
	#869	Ray Davis	$2.8 B	76	pipelines	United States
	#870	Louis Le Duff	$2.8 B	71	bakeries	France
	#871	Chen Fashu	$2.8 B	57	investments	China
	#872	Gil Shwed	$2.8 B	50	software	Israel
	#873	Hanni Toosbuy Kasprzak	$2.8 B	60	shoes	Denmark
	#874	John Dorrance, III.	$2.8 B	74	Campbell Soup	Ireland
	#874	Philip Niarchos	$2.8 B	64	art collection	Greece
	#876	Li Sze Lim	$2.8 B	61	real estate	Hong Kong
	#877	Hans Melchers	$2.8 B	80	chemicals, investments	Netherlands
	#878	John Fisher	$2.8 B	57	Gap	United States
	#879	Glen Taylor	$2.8 B	77	printing	United States
	#880	Vincent Viola	$2.8 B	62	electronic trading	United States
	#881	Doris Fisher	$2.8 B	86	Gap	United States
	#882	Liu Ming Hui	$2.8 B	55	natural gas distribution	China
	#883	Carlos Ardila Lülle	$2.8 B	88	soft drinks, diversified	Colombia
	#884	Bob Parsons	$2.8 B	67	web hosting	United States
	#885	William Wrigley, Jr.	$2.8 B	54	chewing gum	United States
	#886	Hedda im Brahm-Droege	$2.8 B	63	consulting	Germany
	#887	Osman Kibar	$2.8 B	47	biotech	United States
	#888	Scott Lin	$2.8 B	-	optical components	Taiwan
	#889	E. Joe Shoen	$2.7 B	68	U-Haul	United States
	#890	Tsai Hong-tu	$2.7 B	65	finance	Taiwan
	#891	Chandru Raheja	$2.7 B	77	real estate	India
	#892	Spiro Latsis	$2.7 B	71	banking, shipping	Greece
	#893	Rakesh Gangwal	$2.7 B	64	airline	United States
	#894	Eduardo Eurnekian	$2.7 B	85	airports, investments	Argentina
	#895	Erwin Franz Mueller	$2.7 B	85	drugstores	Germany
	#896	Gustav Magnar Witzoe	$2.7 B	25	fish farming	Norway
	#897	James Irsay	$2.7 B	59	Indianapolis Colts	United States
	#898	Mark Stevens	$2.7 B	58	venture capital	United States
	#899	Walter Faria	$2.7 B	63	beer	Brazil
	#900	Lau Cho Kun	$2.7 B	82	palm oil, property	Malaysia
	#901	Mohamed Mansour	$2.7 B	70	diversified	Egypt
	#902	Jerry Yang	$2.7 B	49	Yahoo	United States
	#903	Wang Laichun	$2.7 B	51	electronics components	China
	#904	Kieu Hoang	$2.7 B	74	medical products	United States
	#905	Zygmunt Solorz-Zak	$2.7 B	61	TV broadcasting	Poland
	#906	Chase Coleman, III.	$2.7 B	43	hedge fund	United States
	#907	Ty Warner	$2.7 B	73	real estate, plush toys	United States
	#908	Raj Kumar & Kishin RK	$2.7 B	64	real estate	Singapore
	#909	Park Yeon-Cha	$2.7 B	72	sneakers	South Korea
	#910	Wang Laisheng	$2.7 B	53	electronics components	China
	#911	Dong Wei	$2.7 B	47	pharmaceuticals	China
	#912	Philippe Foriel-Destezet	$2.7 B	82	employment agency	France
	#913	Ralph Sonnenberg	$2.7 B	84	blinds	Netherlands
	#914	Norman Braman	$2.7 B	85	art, car dealerships	United States
	#915	Lawrence Stroll	$2.7 B	58	fashion investments	Canada
	#916	Don Hankey	$2.7 B	75	auto loans	United States
	#917	W. Herbert Hunt	$2.7 B	89	oil	United States
	#918	Aerin Lauder Zinterhofer	$2.7 B	48	cosmetics	United States
	#919	Yu Minhong	$2.7 B	56	education	China
	#920	Robert Miller	$2.7 B	73	electronics components	Canada
	#921	Patrick Ryan	$2.7 B	81	insurance	United States
	#922	Sunny Varkey	$2.7 B	61	education	India
	#923	Torbjorn Tornqvist	$2.7 B	64	oil trading	Sweden
	#924	Mangal Prabhat Lodha	$2.7 B	62	real estate	India
	#925	Warren Stephens	$2.6 B	61	investment banking	United States
	#926	Bradley Jacobs	$2.6 B	62	logistics	United States
	#927	Zuo Hui	$2.6 B	47	real estate services	China
	#928	Jane Lauder	$2.6 B	45	cosmetics	United States
	#929	Daniel Kretinsky	$2.6 B	43	energy generation	Czech Republic
	#930	Kim Beom-Su	$2.6 B	52	online services	South Korea
	#931	Richard Peery	$2.6 B	79	real estate	United States
	#932	Thi Phuong Thao Nguyen	$2.6 B	48	airlines	Vietnam
	#933	Hu Kaijun	$2.6 B	56	pharmaceuticals	China
	#934	Dik Wessels	$2.6 B	72	construction, engineering	Netherlands
	#935	David Bonderman	$2.6 B	75	private equity	United States
	#936	Phillip Ruffin	$2.6 B	83	casinos, real estate	United States
	#937	Koos Bekker	$2.6 B	65	media, investments	South Africa
	#938	Jonathan Gray	$2.6 B	48	investments	United States
	#939	Zhang Hongwei	$2.6 B	63	oil, banking	China
	#940	Taha Mikati	$2.6 B	73	telecom	Lebanon
	#941	Zhang Wenzhong	$2.6 B	56	Retail	China
	#942	Lee Bass	$2.6 B	62	oil, investments	United States
	#943	Remo Ruffini	$2.6 B	56	winter jackets	Italy
	#944	Fiona Geminder	$2.6 B	53	manufacturing	Australia
	#945	Fong Yun Wah	$2.6 B	93	real estate	Hong Kong
	#946	Sean Parker	$2.6 B	38	Facebook	United States
	#947	Phillip T. (Terry) Ragon	$2.6 B	69	health IT	United States
	#948	Mohed Altrad	$2.6 B	70	scaffolding, cement mixers	France
	#949	Bulat Utemuratov	$2.6 B	60	mining, banking, hotels	Kazakhstan
	#950	Timothy Boyle	$2.6 B	68	Columbia Sportswear	United States
	#951	Edward Bass	$2.6 B	72	oil, investments	United States
	#952	Howard Schultz	$2.6 B	64	Starbucks	United States
	#953	Najib Mikati	$2.6 B	62	telecom	Lebanon
	#954	Arkady Rotenberg	$2.6 B	66	construction, pipes, banking	Russia
	#955	Hasmukh Chudgar	$2.6 B	84	pharmaceuticals	India
	#956	John Henry	$2.6 B	68	sports	United States
	#957	C. Dean Metropoulos	$2.5 B	72	investments	United States
	#958	Alfred Gantner	$2.5 B	50	private equity	Switzerland
	#958	Marcel Erni	$2.5 B	53	private equity	Switzerland
	#958	Urs Wietlisbach	$2.5 B	56	private equity	Switzerland
	#961	Kazuo Okada	$2.5 B	75	casinos	Japan
	#962	Anita Zucker	$2.5 B	66	chemicals	United States
	#963	George Bishop	$2.5 B	80	oil & gas	United States
	#964	Lim Sung-Ki	$2.5 B	78	pharmaceuticals	South Korea
	#965	Bill Haslam	$2.5 B	59	truck stops	United States
	#966	Alexander Frolov	$2.5 B	54	mining, steel	Russia
	#967	Stein Erik Hagen	$2.5 B	61	consumer goods	Norway
	#968	Kuan Kam Hon	$2.5 B	70	synthetic gloves	Malaysia
	#969	John Arrillaga	$2.5 B	81	real estate	United States
	#970	Lawrence Ho	$2.5 B	41	casinos	Hong Kong
	#971	Peter Thiel	$2.5 B	50	Facebook, Palantir	United States
	#972	Bennett Dorrance	$2.5 B	72	Campbell Soup	United States
	#973	Juan Abello	$2.5 B	76	investments	Spain
	#974	Li Zhongchu	$2.5 B	54	software	China
	#975	Caroline Hagen Kjos	$2.5 B	34	conglomerate	Norway
	#976	Elaine Wynn	$2.5 B	76	casinos, hotels	United States
	#977	Stephen Lansdown	$2.5 B	65	financial services	Guernsey
	#978	Pollyanna Chu	$2.5 B	60	financial services	Hong Kong
	#979	Stefan Olsson	$2.5 B	69	diversified	Sweden
	#980	Kenneth Feld	$2.5 B	69	circus, live entertainment	United States
	#981	Klaus-Peter Schulenberg	$2.5 B	-	ticketing service	Germany
	#982	Sze Man Bok	$2.5 B	68	hygiene products	China
	#983	Stephan Schmidheiny	$2.5 B	70	investments	Switzerland
	#984	Or Wai Sheun	$2.5 B	67	real estate	Hong Kong
	#985	Michael & Reiner Schmidt-Ruthenbeck	$2.5 B	75	retail	Germany
	#986	Hui Lin Chit	$2.5 B	65	hygiene products	China
	#987	Peter Lim	$2.5 B	65	investments	Singapore
	#988	Bill Gross	$2.5 B	74	investments	United States
	#989	John Caudwell	$2.5 B	65	mobile phones	United Kingdom
	#990	Bert Beveridge	$2.5 B	56	vodka	United States
	#991	T. Denny Sanford	$2.5 B	82	banking, credit cards	United States
	#992	Abilio dos Santos Diniz	$2.5 B	81	retail	Brazil
	#993	Arturo Moreno	$2.5 B	71	billboards, Anaheim Angels	United States
	#994	Tsai Cheng-da	$2.5 B	-	finance	Taiwan
	#995	Noam Gottesman	$2.5 B	57	hedge funds	United States
	#996	Isabel dos Santos	$2.5 B	45	investments	Angola
	#997	Adam Neumann	$2.5 B	39	WeWork	Israel
	#998	Gilles Martin	$2.5 B	54	laboratory services	France
	#999	Ennio Doris	$2.5 B	78	financial services	Italy
	#1000	Eric Smidt	$2.5 B	58	hardware stores	United States
	#1001	Denise York	$2.5 B	67	San Francisco 49ers	United States
	#1002	David Zalik	$2.5 B	44	technology	United States
	#1003	Lam Kong	$2.5 B	54	pharmaceuticals	China
	#1004	George Argyros	$2.5 B	81	real estate, investments	United States
	#1005	Low Tuck Kwong	$2.4 B	70	coal	Indonesia
	#1006	Alexander Spanos	$2.4 B	94	real estate, Los Angeles Chargers	United States
	#1007	Bernard Lewis	$2.4 B	92	fashion retailer	United Kingdom
	#1008	Eva Maria Bucher-Haefner	$2.4 B	61	Computer Associates	Switzerland
	#1009	Jose Luis Cutrale	$2.4 B	71	orange juice	Brazil
	#1010	Wang Wenjing	$2.4 B	53	business software	China
	#1011	John Pritzker	$2.4 B	65	hotels, investments	United States
	#1012	P.V. Ramprasad Reddy	$2.4 B	60	pharmaceuticals	India
	#1013	Peter Buck	$2.4 B	87	Subway sandwich shops	United States
	#1014	Hermann Langness	$2.4 B	65	retail	Germany
	#1015	Hortensia Herrero	$2.4 B	68	supermarkets	Spain
	#1016	Husnu Ozyegin	$2.4 B	73	finance, diversified	Turkey
	#1017	Ramon Ang	$2.4 B	64	Diversified	Philippines
	#1018	Nikolai Buinov	$2.4 B	51	oil, gas	Russia
	#1019	Abhay Firodia	$2.4 B	73	automobiles	India
	#1020	Murli Dhar & Bimal Kumar Gyanchandani	$2.4 B	-	Detergents	India
	#1021	Shen Wenrong	$2.4 B	72	steel production	China
	#1022	Choo Chong Ngen	$2.4 B	65	hotels	Singapore
	#1023	Wu Yulan	$2.4 B	48	pharmaceuticals	China
	#1024	Larry Robbins	$2.4 B	48	hedge funds	United States
	#1025	Michael Ying	$2.4 B	68	retail	Hong Kong
	#1026	Juan-Miguel Villar Mir	$2.4 B	86	construction	Spain
	#1027	Yoshiko Mori	$2.4 B	77	real estate	Japan
	#1028	Daniel Pritzker	$2.4 B	58	hotels, investments	United States
	#1029	Charles Bronfman	$2.4 B	87	liquor	Canada
	#1030	Alan N. Trefler	$2.4 B	62	software	United States
	#1031	Maritsa Lazari	$2.4 B	73	real estate	United Kingdom
	#1032	Chung Eui-Sun	$2.4 B	47	logistics	South Korea
	#1033	Michael Hintze	$2.4 B	64	investment	Australia
	#1034	Igor Kesaev	$2.4 B	51	tobacco distribution, retail	Russia
	#1035	Charles Edelstenne	$2.4 B	80	aviation	France
	#1036	Cho Tak Wong	$2.4 B	72	auto parts	Hong Kong
	#1037	Lu Xiangyang	$2.4 B	55	automobiles, batteries	China
	#1038	Peter Unger	$2.4 B	73	auto repair	Germany
	#1039	Thomas Lau	$2.4 B	64	department stores	Hong Kong
	#1040	Jiang Bin	$2.4 B	51	acoustic components	China
	#1041	Lottie Tham	$2.3 B	69	H&M	Sweden
	#1042	Alexander Mamut	$2.3 B	58	investments	Russia
	#1043	Huang Yi	$2.3 B	56	auto distribution	Hong Kong
	#1044	Mitchell Goldhar	$2.3 B	56	real estate	Canada
	#1045	Horst Julius Pudwill	$2.3 B	73	manufacturing	Germany
	#1046	Oleg Tinkov	$2.3 B	50	banking	Russia
	#1047	Jaime Botin	$2.3 B	82	banking	Spain
	#1048	Alijan Ibragimov	$2.3 B	64	mining, metals	Kazakhstan
	#1049	Alexander Machkevich	$2.3 B	64	mining, metals	Israel
	#1050	Clayton Mathile	$2.3 B	77	pet food	United States
	#1051	Lang Walker	$2.3 B	73	real estate	Australia
	#1052	Huang Wei	$2.3 B	58	real estate	China
	#1053	Luigi Rovati	$2.3 B	89	pharmaceuticals	Italy
	#1054	Tung Chee Hwa	$2.3 B	81	shipping	Hong Kong
	#1055	Francesco Gaetano Caltagirone	$2.3 B	75	cement, diversified	Italy
	#1056	Daniel Mate	$2.3 B	55	mining, commodities	Spain
	#1057	Harsh Mariwala	$2.3 B	67	consumer goods	India
	#1058	John Coates	$2.3 B	48	online gambling	United Kingdom
	#1059	Vinod & Anil Rai Gupta	$2.3 B	72	electrical equipment	India
	#1060	Lutz Mario Helmig	$2.3 B	71	hospitals	Germany
	#1061	Brad Kelley	$2.3 B	61	tobacco	United States
	#1062	Helena Revoredo	$2.3 B	71	security services	Spain
	#1063	J. Joe Ricketts	$2.3 B	76	TD Ameritrade	United States
	#1064	Bernard Fraisse	$2.3 B	61	pharmaceuticals	France
	#1065	Vivien Chen	$2.3 B	59	real estate	Hong Kong
	#1066	Florentino Perez	$2.3 B	71	construction	Spain
	#1067	Murali Divi	$2.3 B	67	pharmaceuticals	India
	#1068	Ermirio Pereira de Moraes	$2.3 B	86	diversified	Brazil
	#1069	Arvind Tiku	$2.3 B	48	oil & gas, investments	India
	#1070	Evan Williams	$2.3 B	46	Twitter	United States
	#1071	Alfred Oetker	$2.3 B	51	consumer goods	Germany
	#1071	August Oetker	$2.3 B	74	consumer goods	Germany
	#1071	Bergit Douglas	$2.3 B	71	consumer goods	Germany
	#1071	Carl Ferdinand Oetker	$2.3 B	45	consumer goods	Germany
	#1071	Christian Oetker	$2.3 B	70	consumer goods	Germany
	#1071	Julia Oetker	$2.3 B	39	consumer goods	Germany
	#1071	Richard Oetker	$2.3 B	67	consumer goods	Germany
	#1071	Rosely Schweizer	$2.3 B	77	consumer goods	Germany
	#1079	Ron Baron	$2.3 B	75	money management	United States
	#1080	Carlo Fidani	$2.3 B	63	real estate	Canada
	#1081	Chang-Woo Han	$2.3 B	87	pachinko parlors	Japan
	#1082	Dan Snyder	$2.3 B	53	Washington Redskins	United States
	#1083	Tong Jinquan	$2.3 B	63	real estate	China
	#1084	An Kang	$2.3 B	69	pharmaceuticals	China
	#1085	Tang Yiu	$2.3 B	84	fashion retail	Hong Kong
	#1086	Ron Burkle	$2.3 B	65	supermarkets, investments	United States
	#1087	Lorenzo Fertitta	$2.3 B	49	casinos, mixed martial arts	United States
	#1088	Roberto Angelini Rossi	$2.3 B	69	forestry, mining	Chile
	#1089	Sunil Vaswani	$2.3 B	54	diversified	United Kingdom
	#1090	Jose and Francisco Jose Calderon Rojas	$2.3 B	-	beverages	Mexico
	#1091	Song Zuowen	$2.3 B	71	aluminum, diversified	China
	#1092	Frank Fertitta, III.	$2.3 B	56	casinos, mixed martial arts	United States
	#1093	Sandro Veronesi	$2.2 B	58	fashion	Italy
	#1094	Mustafa Kucuk	$2.2 B	55	fashion retail	Turkey
	#1095	Stanley Perron	$2.2 B	95	real estate, retail	Australia
	#1096	Chu Lam Yiu	$2.2 B	48	flavorings	Hong Kong
	#1097	Leena Tewari	$2.2 B	60	pharmaceuticals	India
	#1098	Ted Turner	$2.2 B	79	cable television	United States
	#1099	Aristotelis Mistakidis	$2.2 B	56	mining, commodities	Greece
	#1100	Karl Scheufele, III.	$2.2 B	79	jewelry	Switzerland
	#1101	Torstein Hagen	$2.2 B	75	cruises	Norway
	#1102	David Gottesman	$2.2 B	92	investments	United States
	#1103	Drayton McLane, Jr.	$2.2 B	81	Wal-Mart, logistics	United States
	#1104	Stephen Rubin	$2.2 B	81	sports apparel	United Kingdom
	#1105	Chen Jinxia	$2.2 B	50	investments	China
	#1106	Charles Zegar	$2.2 B	70	Bloomberg LP	United States
	#1107	Zhang Fan	$2.2 B	52	touch screens	China
	#1108	Andrew Tan	$2.2 B	65	diversified	Philippines
	#1109	Jorge Moll Filho	$2.2 B	73	hospitals	Brazil
	#1110	Stewart Rahr	$2.2 B	72	drug distribution	United States
	#1111	William Young	$2.2 B	77	plastics	United States
	#1112	Satoshi Suzuki	$2.2 B	64	cosmetics	Japan
	#1113	Thomas Lee	$2.2 B	74	private equity	United States
	#1114	Julio Mario Santo Domingo, III.	$2.2 B	33	beer	United States
	#1114	Tatiana Casiraghi	$2.2 B	34	beer	Monaco
	#1116	Tony Chen	$2.2 B	50	eletronics	Taiwan
	#1117	James Coulter	$2.2 B	58	private equity	United States
	#1118	Jeffrey Lorberbaum	$2.2 B	63	flooring	United States
	#1119	Zhao Tao	$2.2 B	52	pharmaceuticals	Singapore
	#1120	Kuok Khoon Hong	$2.2 B	68	palm oil	Singapore
	#1121	Roberto Irineu Marinho	$2.2 B	70	media	Brazil
	#1122	Jose Roberto Marinho	$2.2 B	62	media	Brazil
	#1123	N.R. Narayana Murthy	$2.2 B	71	software services	India
	#1124	Alec Gores	$2.2 B	65	private equity	United States
	#1125	Eric Lefkofsky	$2.2 B	48	Groupon	United States
	#1126	Harsh Goenka	$2.2 B	60	diversified	India
	#1127	Chen Hua	$2.2 B	52	real estate	China
	#1128	T.Y. Tsai	$2.2 B	-	finance	Taiwan
	#1129	Gao Tianguo	$2.1 B	66	real estate, finance	China
	#1130	Heikki Kyostila	$2.1 B	72	dental products	Finland
	#1131	Ravi Jaipuria	$2.1 B	63	soft drinks	India
	#1132	Kavitark Ram Shriram	$2.1 B	61	venture capital, Google	United States
	#1133	James Clark	$2.1 B	74	Netscape, investments	United States
	#1134	Yu Rong	$2.1 B	46	health clinics	China
	#1135	Steve Conine	$2.1 B	45	online retail	United States
	#1136	Niraj Shah	$2.1 B	44	online retail	United States
	#1137	Maria Helena Moraes Scripilliti	$2.1 B	87	diversified	Brazil
	#1138	Eddie & Sol Zakay	$2.1 B	-	Real Estate	United Kingdom
	#1139	Stanley Hubbard	$2.1 B	85	DirecTV	United States
	#1140	Carlos Sanchez	$2.1 B	56	generic drugs	Brazil
	#1141	Masateru Uno	$2.1 B	71	drugstores	Japan
	#1142	Gordon Getty	$2.1 B	84	Getty Oil	United States
	#1143	Ma Xingtian	$2.1 B	49	pharmaceuticals	China
	#1144	Bahaa Hariri	$2.1 B	52	real estate, investments, logistics	Lebanon
	#1145	Shen Guojun	$2.1 B	55	retail	China
	#1146	Hans-Werner Hector	$2.1 B	78	SAP	Germany
	#1147	Katsumi Tada	$2.1 B	72	real estate	Japan
	#1148	Alain Taravella	$2.1 B	70	real estate	France
	#1149	Tomas Olivo Lopez	$2.1 B	44	shopping centers	Spain
	#1150	Alexey Repik	$2.1 B	38	pharmaceuticals	Russia
	#1151	Zhang Xiugen	$2.1 B	57	automobiles	China
	#1152	Patokh Chodiev	$2.1 B	65	mining, metals	Belgium
	#1153	Carlos Hank Rhon	$2.1 B	70	banking	Mexico
	#1154	James Dinan	$2.1 B	59	hedge funds	United States
	#1155	Aloysio de Andrade Faria	$2.1 B	97	banking	Brazil
	#1156	Shyam & Hari Bhartia	$2.1 B	65	Diversified	India
	#1157	Martin Lau	$2.1 B	45	e-commerce	Hong Kong
	#1158	Erik Selin	$2.1 B	51	real estate	Sweden
	#1159	Prajogo Pangestu	$2.1 B	74	petrochemicals	Indonesia
	#1160	David Walentas	$2.1 B	79	real estate	United States
	#1161	Ferit Faik Sahenk	$2.1 B	54	diversified	Turkey
	#1162	Christian Latouche	$2.1 B	77	accounting services	France
	#1162	Georg von Opel	$2.1 B	52	real estate, investments	Switzerland
	#1162	H. Ross Perot, Jr.	$2.1 B	59	real estate	United States
	#1165	Vadim Moshkovich	$2.1 B	51	agriculture, land	Russia
	#1166	Kwek Leng Beng	$2.1 B	77	real estate	Singapore
	#1167	Maja Oeri	$2.1 B	63	Roche Holding	Switzerland
	#1168	Igor Makarov	$2.1 B	56	investments	Russia
	#1169	Todd Christopher	$2.1 B	55	hair care products	United States
	#1170	Guenther Lehmann	$2.1 B	-	drugstores	Germany
	#1171	Martin Moller Nielsen	$2.1 B	53	aircraft leasing	Denmark
	#1172	Vikas Oberoi	$2.1 B	47	real estate	India
	#1173	Richard Chandler	$2.1 B	59	investments	New Zealand
	#1174	Joao Roberto Marinho	$2.1 B	64	media	Brazil
	#1175	Osathanugrah Family	$2.1 B	-	beverages	Thailand
	#1176	Vincent Lo	$2.1 B	69	real estate	Hong Kong
	#1177	Kevin Plank	$2.1 B	45	Under Armour	United States
	#1178	Maria Franca Fissolo	$2.1 B	83	Nutella, chocolates	Italy
	#1179	Willibert Krueger	$2.1 B	77	food processing	Germany
	#1180	Vivek Chand Burman	$2.1 B	81	consumer goods	India
	#1181	Thomas Hagen	$2.1 B	82	insurance	United States
	#1182	Arvind Poddar	$2.1 B	60	tires	India
	#1183	Anil Ambani	$2.1 B	59	diversified	India
	#1184	Leslie Alexander	$2.1 B	75	sports team	United States
	#1185	Lin Li	$2.1 B	55	investments	China
	#1186	John Tyson	$2.1 B	64	food processing	United States
	#1187	Tang Shing-bor	$2 B	84	real estate	Hong Kong
	#1188	Manuel Jove	$2 B	77	real estate	Spain
	#1189	Liao Long-shing	$2 B	65	petrochemicals	Taiwan
	#1189	Lin Shu-Hong	$2 B	89	petrochemicals	Taiwan
	#1189	Tseng Shin-yi	$2 B	90	petrochemicals	Taiwan
	#1192	Sam Goi	$2 B	69	frozen foods	Singapore
	#1193	Takao Yasuda	$2 B	69	retail	Japan
	#1194	John de Mol	$2 B	63	television	Netherlands
	#1195	Heloise Pratt	$2 B	55	manufacturing, investment	Australia
	#1196	Ye Cheng	$2 B	56	conglomerate	China
	#1197	Jeffrey Lurie	$2 B	66	Philadelphia Eagles	United States
	#1198	David Murdock	$2 B	95	Dole, real estate	United States
	#1199	S. Daniel Abraham	$2 B	93	Slim-Fast	United States
	#1200	Shin Chang-Jae	$2 B	64	insurance	South Korea
	#1201	Francisco Jose Riberas Mera	$2 B	54	steel, autoparts	Spain
	#1202	Dieter Schaub	$2 B	80	media	Germany
	#1203	Alexandra Daitch	$2 B	55	Cargill	United States
	#1203	Katherine Tanner	$2 B	62	Cargill	United States
	#1203	Lucy Stitzer	$2 B	58	Cargill	United States
	#1203	Sarah MacMillan	$2 B	64	Cargill	United States
	#1207	Catherine Lozick	$2 B	73	valve manufacturing	United States
	#1208	David McMurtry	$2 B	78	manufacturing	United Kingdom
	#1209	Glenn Dubin	$2 B	61	hedge funds	United States
	#1210	Antony Ressler	$2 B	56	finance	United States
	#1211	Peter Spuhler	$2 B	58	train cars	Switzerland
	#1212	Wu Kaiting	$2 B	48	electronics	Hong Kong
	#1213	Bob Gaglardi	$2 B	77	hotels	Canada
	#1214	Jiang Yehua	$2 B	55	real estate	China
	#1215	Dermot Desmond	$2 B	68	finance	Ireland
	#1216	Anand Mahindra	$2 B	63	automobiles	India
	#1217	Brian Sheth	$2 B	42	investments	United States
	#1217	Henry Laufer	$2 B	72	hedge funds	United States
	#1217	Thai Lee	$2 B	59	IT provider	United States
	#1220	Philippe Ginestet	$2 B	64	retail stores	France
	#1220	Sylvia Stroeher	$2 B	63	cosmetics	Germany
	#1222	Wong Man Li	$2 B	53	furniture	Hong Kong
	#1223	Mao Lixiang	$2 B	77	cooking appliances	China
	#1224	Josef Boquoi	$2 B	84	frozen foods	Germany
	#1225	Jon Yarbrough	$2 B	61	video games	United States
	#1226	Xue Xiangdong	$2 B	59	software	China
	#1227	Liang Yunchao	$2 B	49	nutrition supplements	China
	#1228	Chin Jong Hwa	$2 B	60	auto parts	Taiwan
	#1229	Li Xiting	$2 B	67	medical devices	China
	#1230	Maurice Alter	$2 B	93	real estate	Australia
	#1231	David Hains	$2 B	87	Investment	Australia
	#1232	Robert Duggan	$2 B	74	pharmaceuticals	United States
	#1233	Andre Esteves	$2 B	49	banking	Brazil
	#1234	Brandt Louie	$2 B	75	drugstores	Canada
	#1235	Mark Coombs	$2 B	57	finance	United Kingdom
	#1236	Bernhard Braun-Luedicke	$2 B	41	medical technology	Germany
	#1236	Eva Maria Braun-Luedicke	$2 B	31	medical technology	Germany
	#1236	Friederike Braun-Luedicke	$2 B	34	medical technology	Germany
	#1239	Andrei Bokarev	$2 B	51	metals, mining	Russia
	#1240	Amy Wyss	$2 B	47	medical equipment	United States
	#1241	Serge Godin	$2 B	68	information technology	Canada
	#1242	Christopher Cline	$2 B	60	coal	United States
	#1243	Bruce Karsh	$2 B	62	private equity	United States
	#1244	William Stone	$2 B	63	software	United States
	#1245	Zhu Baoguo	$1.9 B	56	pharmaceuticals	China
	#1246	Ronald Wanek	$1.9 B	77	furniture	United States
	#1247	Li Zongsong	$1.9 B	51	pharmaceuticals	China
	#1248	Jennifer Pritzker	$1.9 B	67	hotels, investments	United States
	#1249	Lee Myung-Hee	$1.9 B	74	retail	South Korea
	#1250	Christoph Henkel	$1.9 B	60	consumer goods	Germany
	#1251	Yasseen Mansour	$1.9 B	56	diversified	Egypt
	#1252	Howard Marks	$1.9 B	72	private equity	United States
	#1253	Filiz Sahenk	$1.9 B	51	diversified	Turkey
	#1254	Jean-Paul and Martine Clozel	$1.9 B	-	pharmaceuticals	Switzerland
	#1255	Matthias Reinhart	$1.9 B	58	finance	Switzerland
	#1256	Antti Aarnio-Wihuri	$1.9 B	78	diversified	Finland
	#1257	Patrice Motsepe	$1.9 B	56	mining	South Africa
	#1258	Senapathy Gopalakrishnan	$1.9 B	63	software services	India
	#1259	Xiong Xuqiang	$1.9 B	61	real estate	Hong Kong
	#1260	Qi Shi	$1.9 B	48	financial information	China
	#1261	Paolo Bulgari	$1.9 B	80	luxury goods	Italy
	#1262	Saif Al Ghurair	$1.9 B	94	diversified	United Arab Emirates
	#1263	Huang Zhenda	$1.9 B	70	construction	China
	#1264	Mika Anttonen	$1.9 B	51	oil & gas	Finland
	#1265	Wolfgang Leitner	$1.9 B	65	engineering	Austria
	#1266	Zhu Xingliang	$1.9 B	59	construction	China
	#1267	Sarik Tara	$1.9 B	88	construction	Turkey
	#1268	Hilton Schlosberg	$1.9 B	65	energy drinks	United Kingdom
	#1269	Miao Shouliang	$1.9 B	63	real estate	China
	#1270	Yao Kuizhang	$1.9 B	53	beverages	China
	#1271	Ke Xiping	$1.9 B	58	investments	China
	#1272	William Lauder	$1.9 B	58	Estee Lauder	United States
	#1273	Huang Hongyun	$1.9 B	52	real estate	China
	#1274	Strive Masiyiwa	$1.9 B	57	telecom	Zimbabwe
	#1275	Nandan Nilekani	$1.9 B	63	software services	India
	#1276	Wang Jian	$1.9 B	64	healthcare services	China
	#1277	Kishore Mariwala	$1.9 B	83	consumer goods	India
	#1278	Tor Peterson	$1.9 B	53	commodities	United States
	#1279	Supaluck Umpujh & family	$1.9 B	63	retail	Thailand
	#1280	Masahiro Noda	$1.9 B	79	software	Japan
	#1281	Ivan Savvidis	$1.9 B	59	agribusiness	Russia
	#1282	Albert Berner	$1.9 B	82	fasteners	Germany
	#1283	Hamilton James	$1.9 B	66	investments	United States
	#1284	Jim Justice, II.	$1.9 B	67	coal	United States
	#1285	Roberto Hernandez Ramirez	$1.9 B	76	banking	Mexico
	#1286	Chen Jianhua	$1.9 B	47	chemicals	China
	#1287	Shmuel Harlap	$1.9 B	73	automotive	Israel
	#1288	Paul Foster	$1.9 B	60	oil refining	United States
	#1289	Kong Jian Min	$1.9 B	50	real estate	China
	#1290	Chen Yung-Tai	$1.9 B	82	real estate	Taiwan
	#1291	Dulce Pugliese de Godoy Bueno	$1.9 B	70	hospitals, health care	Brazil
	#1292	Wang Liping	$1.9 B	52	hydraulic machinery	China
	#1293	Rodney Sacks	$1.9 B	68	energy drinks	United States
	#1294	Zhu Gongshan	$1.9 B	60	solar panel materials	China
	#1295	Wang Changtian	$1.9 B	53	TV, movie production	China
	#1296	Wang Yanqing	$1.9 B	52	electrical equipment	China
	#1297	Jeffrey Gundlach	$1.9 B	59	investments	United States
	#1298	Krishna Kumar Bangur	$1.9 B	58	graphite electrodes	India
	#1299	Jitendra Virwani	$1.9 B	52	real estate	India
	#1300	Jai Hari & Yadu Hari Dalmia	$1.9 B	-	cement	India
	#1301	Robin Zeng	$1.9 B	50	batteries	Hong Kong
	#1302	Thor Bjorgolfsson	$1.9 B	51	investments	Iceland
	#1303	Sanjiv Goenka	$1.9 B	57	diversified	India
	#1304	David Nahmad	$1.9 B	71	art collection	Monaco
	#1305	Zheng Yuewen	$1.8 B	56	investments	China
	#1306	Ong Beng Seng and Christina Ong	$1.8 B	73	diversified	Singapore
	#1307	He Qiaonv	$1.8 B	52	landscape architecture	China
	#1308	Mario Moretti Polegato	$1.8 B	65	shoes	Italy
	#1309	Anand Burman	$1.8 B	66	consumer goods	India
	#1310	Ranjan Pai	$1.8 B	45	education	India
	#1311	Emilio Azcarraga Jean	$1.8 B	50	TV broadcasting	Mexico
	#1312	Xie Zhikun	$1.8 B	57	investments	China
	#1313	Wichai Thongtang	$1.8 B	71	investments	Thailand
	#1314	Peter Sondakh	$1.8 B	68	investments	Indonesia
	#1315	Li Liufa	$1.8 B	61	steel, diversified	China
	#1316	Dirk Rossmann	$1.8 B	71	drugstores	Germany
	#1317	Richard White	$1.8 B	63	software	Australia
	#1318	Li Li	$1.8 B	54	pharmaceuticals	China
	#1319	Aziz Akhannouch	$1.8 B	57	petroleum, diversified	Morocco
	#1320	Roger Penske	$1.8 B	81	cars	United States
	#1321	Nicola Bulgari	$1.8 B	77	luxury goods	Italy
	#1322	Ren Jianhua	$1.8 B	61	kitchen appliances	China
	#1323	Thaksin Shinawatra	$1.8 B	68	investments	Thailand
	#1324	Lee Boo-Jin	$1.8 B	47	computer services, tourism	South Korea
	#1325	Patricia Angelini Rossi	$1.8 B	64	forestry, mining	Chile
	#1326	Alexander Nesis	$1.8 B	55	metals, banking, fertilizers	Russia
	#1327	James France	$1.8 B	73	Nascar, racing	United States
	#1328	Semahat Sevim Arsel	$1.8 B	89	diversified	Turkey
	#1329	Zhou Xiaoguang	$1.8 B	56	real estate	China
	#1330	Horst Wortmann	$1.8 B	77	footwear	Germany
	#1331	Sergei Gordeev	$1.8 B	45	real estate	Russia
	#1332	Hu Baifan	$1.8 B	55	pharmaceuticals	China
	#1333	Richard Hayne	$1.8 B	70	Urban Outfitters	United States
	#1334	Thomas Bruch	$1.8 B	68	retail	Germany
	#1335	Wang Qingtao	$1.8 B	56	steel smelting	China
	#1336	Jonathan Nelson	$1.8 B	62	private equity	United States
	#1337	Chen Xueli	$1.8 B	67	pharmaceuticals	China
	#1338	Huang Qiaoling	$1.8 B	59	amusement parks	China
	#1339	Aneel Bhusri	$1.8 B	52	business software	United States
	#1340	Nicolas Berggruen	$1.8 B	56	investments	United States
	#1341	Benjamin de Rothschild	$1.8 B	54	banking	Switzerland
	#1342	Gabriel Escarrer	$1.8 B	83	hotels	Spain
	#1343	Petter Stordalen	$1.8 B	55	hotels	Norway
	#1344	Stewart Horejsi	$1.8 B	80	Berkshire Hathaway	United States
	#1345	Yang Erzhu	$1.8 B	67	real estate	China
	#1346	Chen Liying	$1.8 B	42	package delivery	China
	#1347	Bernd Freier	$1.8 B	61	fashion retail	Germany
	#1347	Friedrich Knapp	$1.8 B	67	fashion retail	Germany
	#1349	Luigi Cremonini	$1.8 B	79	meat processing	Italy
	#1350	Manuel Moroun	$1.8 B	91	transportation	United States
	#1351	Linda Pritzker	$1.8 B	64	hotels, investments	United States
	#1352	David Harding	$1.8 B	56	finance	United Kingdom
	#1353	Lee Jay-Hyun	$1.8 B	58	food products, entertainment	South Korea
	#1354	Li Hongxin	$1.8 B	65	paper & related products	China
	#1355	Dou Zhenggang	$1.8 B	65	energy, chemicals	China
	#1356	Kiat Chiaravanont	$1.8 B	-	diversified	Thailand
	#1357	Craig McCaw	$1.8 B	68	telecom	United States
	#1358	Chang Yun Chung	$1.8 B	99	shipping	Singapore
	#1359	Gerald Schwartz	$1.8 B	76	finance	Canada
	#1360	Edward Lampert	$1.8 B	55	Sears	United States
	#1361	Suat Gunsel	$1.8 B	65	real estate, education	Cyprus
	#1362	Zhang Daocai	$1.8 B	68	valves	China
	#1363	Miriam Baumann-Blocher	$1.8 B	43	chemicals	Switzerland
	#1364	Chan Tan Ching-fen	$1.8 B	-	real estate	Hong Kong
	#1365	Hamdi Ulukaya	$1.8 B	45	greek yogurt	Turkey
	#1366	Massimo Moratti	$1.8 B	73	oil refinery	Italy
	#1367	Xiao Yongming	$1.7 B	54	fertilizer	China
	#1368	Mustafa Rahmi Koc	$1.7 B	87	diversified	Turkey
	#1369	Ramesh Juneja	$1.7 B	62	pharmaceuticals	India
	#1370	Faisal Bin Qassim Al Thani	$1.7 B	70	hotels, diversified	Qatar
	#1371	Jean Burelle	$1.7 B	79	automotive systems	France
	#1371	Laurent Burelle	$1.7 B	68	automotive systems	France
	#1373	Julio Bozano	$1.7 B	82	banking	Brazil
	#1374	Murdaya Poo	$1.7 B	77	diversified	Indonesia
	#1375	Mario Gabelli	$1.7 B	76	money management	United States
	#1376	Timothy Headington	$1.7 B	68	oil & gas, investments	United States
	#1377	William Berkley	$1.7 B	71	insurance	United States
	#1378	Edouard Carmignac	$1.7 B	70	asset management	France
	#1379	Ba Duong Tran	$1.7 B	58	automotive	Vietnam
	#1380	Alfredo Egydio Arruda Villela Filho	$1.7 B	48	banking	Brazil
	#1381	N. Murray Edwards	$1.7 B	58	oil & gas	Canada
	#1382	Du Jiangtao	$1.7 B	48	chemicals	China
	#1383	Lee Joong-Keun	$1.7 B	77	construction, real estate	South Korea
	#1384	Shum Chiu Hung	$1.7 B	48	real estate	China
	#1385	Jack Cowin	$1.7 B	75	fast food	Australia
	#1386	William F. Austin	$1.7 B	76	hearing aids	United States
	#1387	Henry Swieca	$1.7 B	61	hedge funds	United States
	#1388	Yin-Chun Wei	$1.7 B	61	food, beverages	Taiwan
	#1389	Miguel McKelvey	$1.7 B	44	WeWork	United States
	#1390	William Koch	$1.7 B	78	oil, investments	United States
	#1391	Geng Jianming	$1.7 B	55	real estate	China
	#1392	Farhad Moshiri	$1.7 B	63	diversified	United Kingdom
	#1393	Wei Yin-Heng	$1.7 B	59	food, beverages	Taiwan
	#1394	Lim Oon Kuin	$1.7 B	74	oil trading	Singapore
	#1395	Monika Schoeller	$1.7 B	79	publishing	Germany
	#1395	Stefan von Holtzbrinck	$1.7 B	55	publishing	Germany
	#1397	Michael Ashcroft	$1.7 B	72	security	United Kingdom
	#1398	Vijay Shekhar Sharma	$1.7 B	40	financial technology	India
	#1399	Vladimir Bogdanov	$1.7 B	67	oil	Russia
	#1400	Herbert Allen, Jr.	$1.7 B	78	investment banking	United States
	#1401	Fritz Draexlmaier	$1.7 B	-	auto parts	Germany
	#1402	Chuchat & Daonapa Petaumpai	$1.7 B	65	motorcycle loans	Thailand
	#1403	Angela Bennett	$1.7 B	74	mining	Australia
	#1404	Li Xuhui	$1.7 B	50	soy sauce maker	China
	#1405	Koon Poh Keong	$1.7 B	57	aluminum	Malaysia
	#1406	Li San Yim	$1.7 B	68	construction equipment	China
	#1407	Juan Maria Riberas Mera	$1.7 B	49	steel	Spain
	#1408	Sheng Jian Zhong	$1.7 B	60	real estate	Singapore
	#1409	David Lichtenstein	$1.7 B	56	real estate	United States
	#1409	Gary Michelson	$1.7 B	69	medical patents	United States
	#1409	Pavel Durov	$1.7 B	33	messaging app	Russia
	#1412	Wei Ying-Chiao	$1.7 B	63	food, beverages	Taiwan
	#1413	Aras Agalarov	$1.7 B	62	real estate	Russia
	#1414	William Fisher	$1.7 B	61	Gap	United States
	#1415	Xiao Wenge	$1.7 B	51	entertainment	China
	#1416	Wang Xicheng	$1.7 B	69	tires	China
	#1417	Lee Seo-Hyun	$1.7 B	44	computer services, tourism	South Korea
	#1418	Liang Feng	$1.7 B	49	manufacturing	China
	#1419	Ruan Shuilong	$1.7 B	82	chemicals	China
	#1420	Wong Luen Hei	$1.7 B	56	building materials	China
	#1421	Marcel Adams	$1.7 B	97	real estate	Canada
	#1422	Willy Michel	$1.7 B	71	medical devices	Switzerland
	#1423	Kevin Systrom	$1.7 B	34	Instagram	United States
	#1424	Yasuhiro Fukushima	$1.7 B	70	video games	Japan
	#1425	Nelson Peltz	$1.7 B	76	investments	United States
	#1426	Anna Maria Braun	$1.7 B	39	medical technology	Germany
	#1426	Johanna Braun	$1.7 B	38	medical technology	Germany
	#1426	Karl Friedrich Braun	$1.7 B	35	medical technology	Germany
	#1429	Marc Lasry	$1.7 B	57	hedge funds	United States
	#1430	Todd Wagner	$1.7 B	57	online media	United States
	#1431	Xu Hang	$1.7 B	52	medical devices	China
	#1432	Wu Guangming	$1.7 B	56	medical equipment	China
	#1433	Su Suyu	$1.7 B	69	utilities, real estate	China
	#1434	Billy Joe (Red) McCombs	$1.7 B	90	real estate, oil, cars, sports	United States
	#1435	Li Guangyu	$1.7 B	54	education	China
	#1436	Konstantin Strukov	$1.7 B	59	gold, coal mining	Russia
	#1437	Qiu Jianping	$1.7 B	56	hand tools	China
	#1438	Robert Fisher	$1.7 B	64	Gap	United States
	#1439	Clement Fayat	$1.7 B	86	construction	France
	#1440	Anthony Langley	$1.7 B	63	manufacturing	United Kingdom
	#1441	Rodney Lewis	$1.7 B	63	natural gas	United States
	#1442	Alexandre Grendene Bartelle	$1.7 B	68	shoes	Brazil
	#1443	Rolf Gerling	$1.7 B	63	insurance	Germany
	#1444	Park Hyeon-Joo	$1.7 B	59	mutual funds	South Korea
	#1445	Lesley Bamberger	$1.7 B	53	real estate	Netherlands
	#1446	Kenneth Lo	$1.7 B	79	textiles	United Kingdom
	#1447	Zhang Wanzhen	$1.7 B	68	electronic components	China
	#1448	Marius Nacht	$1.7 B	52	software	Israel
	#1449	Wei Ing-Chou	$1.7 B	65	food, beverages	Taiwan
	#1450	Michael Jordan	$1.7 B	55	Charlotte Hornets, endorsements	United States
	#1451	John Farber	$1.6 B	92	chemicals	United States
	#1452	Charles Munger	$1.6 B	94	Berkshire Hathaway	United States
	#1453	Jean Salata	$1.6 B	52	finance	Chile
	#1454	Megdet Rahimkulov	$1.6 B	72	investments	Russia
	#1455	Pan Weiming	$1.6 B	54	real estate	China
	#1456	Gregorio Perez Companc	$1.6 B	82	oil & gas	Argentina
	#1457	Wang Chaobin	$1.6 B	62	real estate	China
	#1458	Shi Yuzhu	$1.6 B	55	online games, investments	China
	#1459	Mark Pincus	$1.6 B	52	online games	United States
	#1460	Diego Della Valle	$1.6 B	64	shoes	Italy
	#1461	Ma Xiuhui	$1.6 B	47	LED lighting	China
	#1462	Lia Maria Aguiar	$1.6 B	80	banking	Brazil
	#1463	Ludwig Theodor Braun	$1.6 B	28	medical technology	Germany
	#1464	Khalifa Bin Butti Al Muhairi	$1.6 B	39	hospitals, investments	United Arab Emirates
	#1465	Jayme Garfinkel	$1.6 B	72	insurance	Brazil
	#1466	Huang Chulong	$1.6 B	59	real estate	Canada
	#1467	Keeree Kanjanapas	$1.6 B	67	transportation	Thailand
	#1468	Stefano Gabbana	$1.6 B	55	luxury goods	Italy
	#1469	Vito Rodriguez Rodriguez	$1.6 B	79	processed milk	Peru
	#1470	Roman Trotsenko	$1.6 B	47	transport, engineering, real estate	Russia
	#1471	Dominique Desseigne	$1.6 B	73	casinos	France
	#1472	Lachhman Das Mittal	$1.6 B	87	tractors	India
	#1473	Thomas Steyer	$1.6 B	61	hedge funds	United States
	#1474	Li Guoqiang	$1.6 B	54	auto dealerships	China
	#1475	Brian Roberts	$1.6 B	59	Comcast	United States
	#1476	Kommer Damen	$1.6 B	74	shipbuilding	Netherlands
	#1477	John Whittaker	$1.6 B	76	real estate	United Kingdom
	#1478	Myron Wentz	$1.6 B	78	health products	St. Kitts and Nevis
	#1479	Vladimir Yevtushenkov	$1.6 B	69	telecom, investments	Russia
	#1480	Alex Beard	$1.6 B	50	mining, commodities	United Kingdom
	#1481	Ou Zongrong	$1.6 B	54	real estate	China
	#1482	Brian Higgins	$1.6 B	53	hedge funds	United States
	#1482	Louis Bacon	$1.6 B	61	hedge funds	United States
	#1482	Melih Abdulhayoglu	$1.6 B	50	internet security	Turkey
	#1482	O. Francis Biondi	$1.6 B	54	hedge funds	United States
	#1486	Huo Qinghua	$1.6 B	57	coal	China
	#1487	Mohamed Al Fayed	$1.6 B	89	retail, investments	Egypt
	#1488	Anurang Jain	$1.6 B	56	auto parts	India
	#1489	Ana Lucia de Mattos Barretto Villela	$1.6 B	44	banking	Brazil
	#1490	Domenico Dolce	$1.6 B	59	luxury goods	Italy
	#1491	Kim Jun-Ki	$1.6 B	73	diversified	South Korea
	#1492	Francois Feuillet	$1.6 B	69	motorhomes, RVs	France
	#1493	Liang Jiankun	$1.6 B	57	cobalt mining	China
	#1494	Yusuf Hamied	$1.6 B	81	pharmaceuticals	India
	#1495	David Booth	$1.6 B	72	mutual funds	United States
	#1496	Robert Mouawad	$1.6 B	73	fine jewelry	Lebanon
	#1497	Prayudh Mahagitsiri	$1.6 B	72	coffee, shipping	Thailand
	#1498	Wu Jianshu	$1.6 B	54	auto parts	Hong Kong
	#1499	Lei Jufang	$1.6 B	65	pharmaceuticals	China
	#1500	Alberto Prada	$1.6 B	-	luxury goods	Italy
	#1500	Marina Prada	$1.6 B	-	luxury goods	Italy
	#1502	John Bloor	$1.6 B	75	real estate, manufacturing	United Kingdom
	#1503	Christopher Goldsbury	$1.6 B	75	salsa	United States
	#1504	Cheung Yan	$1.6 B	61	paper manufacturing	China
	#1505	Bill Alfond	$1.6 B	70	shoes	United States
	#1505	Ted Alfond	$1.6 B	73	shoes	United States
	#1507	Somphote Ahunai	$1.6 B	51	energy	Thailand
	#1508	Ben Silbermann	$1.6 B	35	Pinterest	United States
	#1509	Wang Yaohai	$1.6 B	51	lighting	China
	#1510	Susan Alfond	$1.6 B	72	shoes	United States
	#1511	Suna Kirac	$1.6 B	77	diversified	Turkey
	#1512	Nihat Ozdemir	$1.6 B	68	diversified	Turkey
	#1512	Sezai Bacaksiz	$1.6 B	68	diversified	Turkey
	#1514	Jonathan Tisch	$1.6 B	64	insurance, NFL team	United States
	#1515	Bharat Desai	$1.6 B	65	IT consulting	United States
	#1516	Sheryl Sandberg	$1.6 B	48	Facebook	United States
	#1517	Sun Shoukuan	$1.6 B	68	metals. coal	China
	#1518	Alexander Dzhaparidze	$1.6 B	62	oil services	Russia
	#1519	Forrest Preston	$1.6 B	85	health care	United States
	#1520	Stephen Jarislowsky	$1.6 B	92	money management	Canada
	#1521	Ilkka Herlin	$1.6 B	59	elevators, escalators	Finland
	#1522	William Heinecke	$1.6 B	69	hotels	Thailand
	#1523	Stephen Feinberg	$1.6 B	58	private equity	United States
	#1524	Hoi Kin Hong	$1.6 B	65	real estate	Macau
	#1525	Kim Taek-Jin	$1.6 B	51	online games	South Korea
	#1526	Syed Mokhtar AlBukhary	$1.6 B	66	engineering, energy, construction	Malaysia
	#1527	Alberto Cortina	$1.5 B	72	investments	Spain
	#1528	Brunello Cucinelli	$1.5 B	64	fashion	Italy
	#1529	Binod Chaudhary	$1.5 B	63	diversified	Nepal
	#1530	Roman Avdeev	$1.5 B	50	banking, development	Russia
	#1531	Kenneth Tuchman	$1.5 B	58	outsourcing	United States
	#1532	Andrey Andreev	$1.5 B	44	online dating	United Kingdom
	#1533	Ana Maria Brescia Cafferata	$1.5 B	94	mining, banking	Peru
	#1534	Asok Kumar Hiranandani	$1.5 B	63	real estate	Singapore
	#1535	Tobi Lutke	$1.5 B	37	e-commerce	Canada
	#1536	Carol Jenkins Barnett	$1.5 B	61	Publix supermarkets	United States
	#1537	Pierre Karl Péladeau	$1.5 B	56	media	Canada
	#1538	Gavril Yushvaev	$1.5 B	60	precious metals, real estate	Russia
	#1539	Evgeny (Eugene) Shvidler	$1.5 B	54	oil & gas, investments	United States
	#1540	Charlotte Colket Weber	$1.5 B	75	Campbell Soup	United States
	#1541	Hubertus Benteler	$1.5 B	71	auto parts	Germany
	#1542	Folorunsho Alakija	$1.5 B	67	oil	Nigeria
	#1543	Jacques D'Amours	$1.5 B	61	retail	Canada
	#1544	Lee Ho-Jin	$1.5 B	55	diversified	South Korea
	#1545	Alberto Alcocer	$1.5 B	75	investments	Spain
	#1546	Mohammed Dewji	$1.5 B	43	diversified	Tanzania
	#1547	Fayez Sarofim	$1.5 B	89	money management	United States
	#1548	Hal Jackman	$1.5 B	86	insurance, investments	Canada
	#1549	Elisabeth Badinter & family	$1.5 B	74	advertising	France
	#1550	Zhou Chengjian	$1.5 B	53	fashion retail	China
	#1551	Zhou Yaoting	$1.5 B	75	apparel, real estate	China
	#1552	Alexander Klyachin	$1.5 B	51	real estate	Russia
	#1553	Susumu Fujita	$1.5 B	45	internet media	Japan
	#1554	Peter Leibinger	$1.5 B	51	machine tools	Germany
	#1554	Regine Leibinger	$1.5 B	55	machine tools	Germany
	#1556	Othman Benjelloun	$1.5 B	85	banking, insurance	Morocco
	#1557	Lucio and Susan Co	$1.5 B	63	retail	Philippines
	#1558	Albert Yeung	$1.5 B	75	real estate, retail	Hong Kong
	#1559	Nicholas Pritzker, II.	$1.5 B	74	hotels, investments	United States
	#1560	Erik Paulsson	$1.5 B	76	construction, real estate	Sweden
	#1561	Stelios Haji-Ioannou	$1.5 B	51	EasyJet	Cyprus
	#1562	George Joseph	$1.5 B	96	insurance	United States
	#1563	Joao Alves de Queiroz Filho	$1.5 B	65	pharmaceuticals	Brazil
	#1564	Frank Stronach	$1.5 B	85	auto parts	Canada
	#1565	Yuri Shefler	$1.5 B	50	alcohol	Russia
	#1566	Robert Defares	$1.5 B	56	electronic trading	Netherlands
	#1567	Julia Stoschek	$1.5 B	43	auto parts	Germany
	#1567	Maximilian Stoschek	$1.5 B	-	auto parts	Germany
	#1569	Torsten Toeller	$1.5 B	52	pet food	Germany
	#1570	Herb Chambers	$1.5 B	76	car dealerships	United States
	#1571	Wang Jinshu	$1.5 B	61	chemicals	China
	#1572	Arkady Volozh	$1.5 B	54	search engine	Russia
	#1573	Pier Luigi Loro Piana	$1.5 B	66	fashion	Italy
	#1574	Harald Link	$1.5 B	63	diversified	Thailand
	#1575	Ezra Nahmad	$1.5 B	72	art	Monaco
	#1575	Seth Klarman	$1.5 B	61	investments	United States
	#1575	Zhang Tao	$1.5 B	45	e-commerce	China
	#1578	Li Yihai	$1.5 B	55	pharmaceuticals	China
	#1579	Johannes Kaercher	$1.5 B	67	vacuums, cleaning products	Germany
	#1579	Susanne Zimmermann von Siefart 	$1.5 B	61	vacuums, home cleaning products	Germany
	#1581	Tian Ming	$1.5 B	64	measuring instruments	China
	#1582	Liu Ming Chung	$1.5 B	55	paper manufacturing	Brazil
	#1583	Li Liangbin	$1.5 B	50	lithium	China
	#1584	Yuriy Kosiuk	$1.5 B	50	agriculture	Ukraine
	#1585	Cui Genliang	$1.5 B	60	electric components	China
	#1586	Dmitry Pumpyansky	$1.5 B	54	steel pipes	Russia
	#1587	Wu Xu	$1.5 B	54	real estate	St. Kitts and Nevis
	#1588	Shamsheer Vayalil	$1.5 B	41	healthcare	India
	#1589	Radhe Shyam Agarwal	$1.5 B	73	consumer goods	India
	#1589	Radhe Shyam Goenka	$1.5 B	72	consumer goods	India
	#1591	Nobutada Saji	$1.5 B	72	beverages	Japan
	#1592	Oleg Boyko	$1.5 B	53	diversified	Russia
	#1593	Rufino Vigil Gonzalez	$1.5 B	70	steel	Mexico
	#1594	Gao Dekang & family	$1.5 B	66	apparel	China
	#1595	Martha Ford	$1.5 B	92	Ford Motor	United States
	#1596	Jiang Yintai	$1.5 B	67	auto parts	China
	#1597	Theodore Rachmat	$1.5 B	74	diversified	Indonesia
	#1598	Karl-Johan Persson	$1.5 B	43	H&M	Sweden
	#1599	Tom Persson	$1.5 B	33	H&M	Sweden
	#1600	Charlotte Soderstrom	$1.5 B	41	H&M	Sweden
	#1601	P.N.C. Menon	$1.5 B	69	real estate	Oman
	#1602	Djoko Susanto	$1.5 B	68	supermarkets	Indonesia
	#1603	Chang Pyung-Soon	$1.5 B	67	educational services	South Korea
	#1604	Ian Wood	$1.5 B	75	energy services	United Kingdom
	#1605	Chua Thian Poh	$1.5 B	69	real estate	Singapore
	#1606	Anant Asavabhokhin & family	$1.5 B	67	real estate	Thailand
	#1607	Xu Xudong	$1.5 B	48	auto parts	China
	#1608	Alberto Roemmers	$1.5 B	91	pharmaceuticals	Argentina
	#1609	Lin Ming-hsiung	$1.5 B	68	supermarkets	Taiwan
	#1610	Mofatraj Munot	$1.5 B	73	real estate	India
	#1611	Devendra Jain	$1.5 B	89	chemicals	India
	#1612	Mehmet Nazif Gunal	$1.5 B	70	tourism, construction	Turkey
	#1613	Thomas Sandell	$1.5 B	57	hedge funds	Sweden
	#1614	Qin Hui	$1.4 B	50	movie theaters	China
	#1615	Stephen T. Winn	$1.4 B	71	real estate services	United States
	#1616	Beda Diethelm	$1.4 B	77	hearing aids	Switzerland
	#1617	Marcos Galperin	$1.4 B	-	e-commerce	Argentina
	#1618	Ni Zugen	$1.4 B	61	appliances	China
	#1619	Richard Desmond	$1.4 B	66	publishing	United Kingdom
	#1620	Henry Cheng	$1.4 B	71	property	Hong Kong
	#1621	Jerry Reinsdorf	$1.4 B	82	sports teams	United States
	#1622	Markus Persson	$1.4 B	39	computer games	Sweden
	#1623	Youssef Mansour	$1.4 B	73	diversified	Egypt
	#1624	Alexandra Andresen	$1.4 B	21	investments	Norway
	#1624	Katharina Andresen	$1.4 B	23	investments	Norway
	#1626	Reinold Geiger	$1.4 B	71	beauty products	Austria
	#1627	William Li	$1.4 B	43	automobiles	China
	#1628	Sefik Yilmaz Dizdar	$1.4 B	80	fashion retail	Turkey
	#1629	Edmund Ansin	$1.4 B	82	television	United States
	#1630	Ilona Herlin	$1.4 B	53	elevators, escalators	Finland
	#1631	Pyotr Kondrashev	$1.4 B	68	investments	Russia
	#1632	Luis Enrique Yarur Rey	$1.4 B	67	banking	Chile
	#1633	Xiao Chunhong	$1.4 B	50	real estate	China
	#1634	Kirill Shamalov	$1.4 B	36	petrochemicals	Russia
	#1635	Mark Dixon	$1.4 B	59	office real estate	United Kingdom
	#1636	James Leininger	$1.4 B	73	medical products	United States
	#1637	Gail Miller	$1.4 B	74	basketball, car dealers	United States
	#1638	Zhou Bajin	$1.4 B	83	auto parts	China
	#1639	Victor Pinchuk	$1.4 B	57	steel pipes, diversified	Ukraine
	#1640	Anatoly Lomakin	$1.4 B	66	investments	Russia
	#1641	Jerry Moyes	$1.4 B	74	Transportation	United States
	#1642	Wong Kwong Yu	$1.4 B	49	retail	China
	#1643	Jim Thompson	$1.4 B	78	logistics	United States
	#1644	Bhadresh Shah	$1.4 B	66	engineering	India
	#1645	Anton Rabie	$1.4 B	46	toys	Canada
	#1645	Ronnen Harary	$1.4 B	46	toys	Canada
	#1647	Polys Haji-Ioannou	$1.4 B	58	EasyJet	Cyprus
	#1648	Niranjan Hiranandani	$1.4 B	68	real estate	India
	#1649	Hur Young-In	$1.4 B	69	bakeries, fast food	South Korea
	#1650	Richard Yuengling, Jr.	$1.4 B	75	beer	United States
	#1651	K. Dinesh	$1.4 B	64	software services	India
	#1652	Zhao Weiguo	$1.4 B	51	IT products	China
	#1653	Kutayba Alghanim	$1.4 B	72	diversified	Kuwait
	#1654	Gary Fegel	$1.4 B	44	commodities, investments	Switzerland
	#1655	Solomon Lew	$1.4 B	73	retail	Australia
	#1656	John Edson	$1.4 B	86	leisure craft	United States
	#1657	Kenny Troutt	$1.4 B	70	telecom	United States
	#1658	Thomas Wu	$1.4 B	68	finance	Taiwan
	#1659	Carl Douglas	$1.4 B	57	investments	Sweden
	#1659	Eric Douglas	$1.4 B	50	investments	Sweden
	#1661	Kentaro Ogawa	$1.4 B	70	restaurants	Japan
	#1662	Maria Del Pino y Calvo-Sotelo	$1.4 B	62	construction	Spain
	#1663	Wilma Tisch	$1.4 B	91	diversified	United States
	#1664	Allan Wong	$1.4 B	68	electronics	Hong Kong
	#1665	Peter Sperling	$1.4 B	58	education	United States
	#1666	Andre Koo	$1.4 B	51	financial services	Taiwan
	#1667	Alan Gerry	$1.4 B	89	cable television	United States
	#1667	John Armitage	$1.4 B	58	hedge funds	Ireland
	#1667	Philippe Laffont	$1.4 B	50	hedge fund	United States
	#1670	Anne Gittinger	$1.4 B	82	Nordstrom department stores	United States
	#1671	B. Wayne Hughes, Jr.	$1.4 B	57	storage facilities	United States
	#1672	Joy Alukkas	$1.4 B	61	jewelry	India
	#1673	Michael Krasny	$1.4 B	64	retail	United States
	#1674	Changpeng Zhao	$1.4 B	-	cryptocurrency	China
	#1675	Oei Hong Leong	$1.4 B	70	investments	Singapore
	#1676	Leonard Schleifer	$1.4 B	66	pharmaceuticals	United States
	#1677	John Kapoor	$1.4 B	74	healthcare	United States
	#1678	Dan Wilks	$1.4 B	62	natural gas	United States
	#1679	Bassam Alghanim	$1.4 B	66	diversified	Kuwait
	#1680	Farris Wilks	$1.4 B	66	natural gas	United States
	#1681	J. Tomilson Hill	$1.4 B	70	investments	United States
	#1682	Mori Arkin	$1.4 B	65	pharmaceuticals	Israel
	#1683	Gerry Harvey	$1.4 B	78	retail	Australia
	#1684	Rana Kapoor	$1.4 B	60	banking	India
	#1685	Thomas Meyer	$1.4 B	59	apparel retailer	Switzerland
	#1686	Nicola Leibinger-Kammueller	$1.4 B	58	manufacturing	Germany
	#1687	Vasily Anisimov	$1.4 B	66	real estate	Russia
	#1688	Fu Guangming	$1.4 B	64	poultry	China
	#1689	Len Ainsworth	$1.4 B	94	betting machines	Australia
	#1690	Kim Nam-Jung	$1.4 B	45	food	South Korea
	#1691	Eugene Kaspersky	$1.4 B	52	software	Russia
	#1692	Manny Stul	$1.4 B	69	toys	Australia
	#1693	Zhang Yubai	$1.4 B	53	wine	China
	#1694	Lou Zhongfu	$1.4 B	64	real estate	China
	#1695	Chen Tianqiao	$1.4 B	45	online games	China
	#1696	Douglas Hsu	$1.4 B	75	diversified	Taiwan
	#1697	Ahmet Calik	$1.4 B	60	energy, banking, construction	Turkey
	#1698	Donald Foss	$1.4 B	74	auto loans	United States
	#1699	Su Rubo	$1.4 B	63	real estate	China
	#1700	Sol Daurella	$1.4 B	52	Coca-Cola	Spain"""
for line in s.splitlines():
    line = line.replace('|', '').split()
    try:
        index = [i for i, s in enumerate(line) if '$' in s][0]

        age = float(line[index + 2])
        wealth = float(line[index].strip('$'))

        plt.plot(age, wealth, 'or')
        plt.annotate(" ".join(line[1:index]), (age, wealth))
    except ValueError:
        print(line)
plt.xlabel('Age')
plt.ylabel('Wealth')
plt.ylim(bottom=0)
plt.show()
