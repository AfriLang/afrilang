"""
original stopwords taken from  International Journal of Computer and Information Technology (ISSN: 2279 – 0764)
credit Asubiaro, Toluwase Victor E. Latunde Odeku Medical Library University of Ibadan Ibadan, Nigeria
"""


_stopwords_diacritics = frozenset('''tí, ni, wọn, àwọn, tó, pé, ń, ṣe, náà, ó, kò, sí, bá, wá, fi, kí, lọ,
 yìí, kan, a, jẹ́, sì, fún, ti, bí, yóò, sọ, àti, rẹ, láti, wó ̣n, ẹ, ní, í, ló, máa, òun, gbà, nínú, 
 rí, gbogbo, nígbà, lè, ọmọ, gbé, ọ̀rọ̀, èyí, mo, mọ, mọ́, rẹ̀, di, ọ̀hún, bẹ́ẹ̀, tún, nǹkan, ara, nítorí, 
 ṣùgbọ́n, lọ́wọ́, mú, dá, lórí, ẹni, ọwọ́, bíi, jù, pẹ̀lú, ọjọ́, mi, sílẹ̀, iṣẹ́, bó, ohun, kó, un, dé, 
 báyìí, pa, níbẹ̀, ibi,  wà, ká,  tàbí,  láàrin, yẹ, gbọ́ , làwọn, bẹ̀rẹ̀, má, ìyẹn, kú, ìgbà, kọjá, 
 lóun, eré, ọnà, pọ̀, àsìkò, jáde, gẹ́gẹ́, jọ, á, i, sọ̀rọ̀, fẹ́, irú, kúrò, bọ̀, o, le, lára, wáá, níbi, 
 lẹ́yìn, wò,  wo, nípa, ín, inú, méjì, nílé, yín, ọn, ńkọ́, ńlá, já,  déédé,  la, tẹ,  rárá,  ìdí, 
 òpin,  ṣeé, lọ́jọ́, lọ́sẹ̀, títí, wáyé,  ò, padà, án,  lójú, tẹ́lẹ̀, rò, gan,  tàwọn,  tán, rán,  tòun, 
  lọọ, ẹ̀yin, ọ̀dọ̀, wa,  tóó, ṣẹbọ, kọ́kọ́,  ta, sá, n, yọ, dúró, hàn, ṣiṣẹ́, lọ́dún, kì, lẹ, ṣẹlẹ̀, pàápàá,
   nílùú, nìkan, níṣẹ́, síbẹ̀, nìyẹn, yẹn, kankan, bóyá,  múra,  fáwọn,  e,  lọ́nà,  yá,  gbọ́dọ̀,  lẹ́nu, 
    wàhálà,  wí, káàkiri,  parí,  síbi,  kọ,  mẹ́ta,  ọ̀kan,  kẹta,  san,  péré,  dáadáa, láìpẹ́, wọlé,
     sùn, tilẹ̀, lélẹ̀, ẹnikẹ́ni, á, ẹnìkan, èmi, ọ̀pọ̀, mẹ́rin, peléke, nídìí, wẹ́wẹ́, ún, méjìlá, kínní, ú,
      sínú, sáré, kín, yàrá, fúnra, kọjú, díẹ̀, lòótọ́, nìyí, àtàwọn, bákan, méjèèjì, fẹ̀gbẹ́, àbí, kiri,
        torí,  jẹ,  káwọn,  márún,  jùlọ,  ọ̀pọ̀lọpọ̀,  síwájú,  àgàgà, lásán, tọ, tètè, àwa, odidi, 
        pàdé, tiẹ, tuntun, gba, sọ́dọ̀, kàn, yí, ọ, mìíràn, wọ̀nyí, ná, ọ́, ẹ́, afi.'''.split())

_stopwords = frozenset(''' ti, ni, won, awon, n, pe, to, si, o, ko, naa, se, lo, wa, ba, e, ki, 
kan, fi, yii, je, i,  fun, a, mo,  yoo, so, re,  bi, le, ati,  lati, gbe, ohun, maa, oun, ninu,
 ile, gba, omo, gbogbo, ri, oro, nigba, un, bee, de,  ka, pa, owo, nitori, egbe, sugbon, lowo,
  on, bo, mu, tun, ara, di, lori, da, benikan, in, eni, fin, wo, eyi, jo, nnkan, mi, te, ise,
   pelu, oju, ilu, ede, ojo, gbo, yin, fee, lawon, bayii, bii, bere,  ju, ebi, daa, ma,  fe, 
   ye, bu,  iyen, jeun, gege,  tabi, waa, gege, tabi, nibi, ta,  leyin, lara, an, meji, iru,
    nibe,  nipa, jade, koja, titi, nla, pada, inu, tele, okan, tawon, tan, loju, too, yo, loun, 
     emi, po, rara,  gbodo, sa, han,  koko, sele,  paapaa, nikan, laarin, see, yen, niyen, ran,
      kuro, ya, meta, iroyin, gan, daadaa, sibe, toun, keji, Kankan, wonyi, laipe, eyin, kinni,
       die, kun,  bakan, bawo,  pari,  atawon,  sinu,  kawon, dara,  siwaju, opolopo, kiri, merin, 
       pade, enikan, niyi, yato, boya, looto, tete, eleyii, kin,  marun, lodun,  saa, tuntun,  rere, 
       seni, sibi,  fowo, koju, dide, yi '''.split())
