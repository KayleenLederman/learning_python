# Make a program that translates mRNA into protein
# It should report the longest ORF in each mRNA - usually assumed to be protein
# Make sure you translate all 3 reading frames on both strands
# It should use argparse and your library, of course

#get reverse complement of seq
#send to translation function

import mcb185
import argparse

# setup
parser = argparse.ArgumentParser(description='Translate mRNA to protein')
# required arguments
parser.add_argument('--file', required=True, type=str,
	metavar='<str>', help='required fasta file')
# finalization
arg = parser.parse_args()


longest_orfs = []
for name, seq in mcb185.read_fasta(arg.file):
	orfseqs_fwd = mcb185.orfseqs(seq)
	orfseqs_fwd.sort(key = len)
	longest_orf_fwd = orfseqs_fwd[-1]
	
	anti = mcb185.anti(seq)
	orfseqs_rev = mcb185.orfseqs(anti)
	orfseqs_rev.sort(key = len)
	longest_orf_rev = orfseqs_rev[-1]
	
	print(name)
	if len(longest_orf_fwd) > len(longest_orf_rev): print(mcb185.translate(longest_orf_fwd))
	else: print(mcb185.translate(longest_orf_rev))

"""
python3 translate_mRNA.py --fasta hs_rna.fa
>NM_001368885.1
MVAERTHKAAATGARGPGELGAPGTVALVAARAERGARLPSPGSCGLLTLALCSLALSLLAHFRTAELQARVLRLEAERG
EQQMETAILGRVNQLLDEKWKLHSRRRREAPKTSPGCNCPPGPPGPTGRPGLPGVKGQPGEKGSPGDAGLSIIGPRGPPG
QPGTRGFPGFPGPIGLDGKPGHPGPKGDMGLTGPPGQPGPQGQKGEKGQCGEYPHRLLPLLNSVRLAPPPVIKRRTFQGE
QSQASIQGPPGPPGPPGPSGPLGHPGLPGPMGPPGLPGPPGPKGDPGIQGYHGRKGERGMPGMPGKHGAKGAPGIAVAGM
KGEPGIPGTKGEKGAEGSPGLPGLLGQKGEKGDAGNSIGGGRGEPGPPGLPGPPGPKGEAGVDGQVGPPGQPGDKGERGA
AGEQGPDGPKGSKGEPGKGEMVDYNGNINEALQEIRTLALMGPPGLPGQIGPPGAPGIPGQKGEIGLPGPPGHDGEKGPR
GKPGDMGPPGPQGPPGKDGPPGVKGENGHPGSPGEKGEKGETGQAGSPGLQGVPGPKGEAGLDGAKGEKGFQGEKGDRGP
LGLPGTPGPIGVPGPAGPKGERGSKGDPGMTGPTGAAGLPGLHGPPGDKGNRGHRGFKGEKGEPGLPGLDGLDAPCPLGE
DGLPVQGCWNK
>NM_001368886.1
MGLTGPPGQPGPQGQKGEKGQCGEYPHRLLPLLNSVRLAPPPVIKRRTFQGEQSQASIQGPPGPPGPPGPSGPLGHPGLP
GPMGPPGLPGPPGPKGDPGIQGYHGRKGERGMPGMPGKHGAKGAPGIAVAGMKGEPGIPGTKGEKGAEGSPGLPGLLGQK
GEKGDAGNSIGGGRGEPGPPGLPGPPGPKGEAGVDGQVGPPGQPGDKGERGAAGEQGPDGPKGSKGEPGKGEMVDYNGNI
NEALQEIRTLALMGPPGLPGQIGPPGAPGIPGQKGEIGLPGPPGHDGEKGPRGKPGDMGPPGPQGPPGKDGPPGVKGENG
HPGSPGEKGEKGETGQAGSPVPGLPGPEGPPGPPGLQGVPGPKGEAGLDGAKGEKGFQGEKGDRGPLGLPGTPGPIGVPG
PAGPKGERGSKGDPGMTGPTGAAGLPGLHGPPGDKGNRGHRGFKGEKGEPGLPGLDGLDAPCPLGEDGLPVQGCWNK
>NR_148047.2
MILSWWLYVHKYIRHLSKLIECIIPRANSNVNYGLWIIMIHQCRFIDCSKCTTLVWDVDSGEAICVGVGGVWELSVLSSQ
FSCESKTALKK
>NR_148053.2
MILSWWLYVHKYIRHLSKLIECIIPRANSNVNYGLWIIMIHQCRFIDCSKCTTLVWDVDSGEAICVGVGGVWELSVLSSQ
FSCESKTALKK
>NM_001374457.1
MSTPDPPLGGTPRPGPSPGPGPSPGAMLGPSPGPSPGSAHSMMGPSPGPPSAGHPIPTQGPGGYPQDNMHQMHKPMESMH
EKGMSDDPRYNQMKGMGMRSGGHAGMGPPPSPMDQHSQGYPSPLGGSEHASSPVPASGPSSGPQMSSGPGGAPLDGADPQ
ALGQQNRGPTPFNQNQLHQLRAQIMAYKMLARGQPLPDHLQMAVQGKRPMPGMQQQMPTLPPPSVSATGPGPGPGPGPGP
GPGPAPPNYSRPHGMGGPNMPPPGPSGVPPGMPGQPPGGPPKPWPEGPMANAAAPTSTPQKLIPPQPTGRPSPAPPAVPP
AASPVMPPQTQSPGQPAQPAPMVPLHQKQSRITPIQKPRGLDPVEILQEREYRLQARIAHRIQELENLPGSLAGDLRTKA
TIELKALRLLNFQRQLRQEVVVCMRRDTALETALNAKAYKRSKRQSLREARITEKLEKQQKIEQERKRRQKHQEYLNSIL
QHAKDFKEYHRSVTGKIQKLTKAVATYHANTEREQKKENERIEKERMRRLMAEDEEGYRKLIDQKKDKRLAYLLQQTDEY
VANLTELVRQHKAAQVAKEKKKKKKKKKAENAEGQTPAIGPDGEPLDETSQMSDLPVKVIHVESGKILTGTDAPKAGQLE
AWLEMNPGYEVAPRSDSEESGSEEEEEEEEEEQPQAAQPPTLPVEEKKKIPDPDSDDVSEVDARHIIENAKQDVDDEYGV
SQALARGLQSYYAVAHAVTERVDKQSALMVNGVLKQYQIKGLEWLVSLYNNNLNGILADEMGLGKTIQTIALITYLMEHK
RINGPFLIIVPLSTLSNWAYEFDKWAPSVVKVSYKGSPAARRAFVPQLRSGKFNVLLTTYEYIIKDKHILAKIRWKYMIV
DEGHRMKNHHCKLTQVLNTHYVAPRRLLLTGTPLQNKLPELWALLNFLLPTIFKSCSTFEQWFNAPFAMTGEKVDLNEEE
TILIIRRLHKVLRPFLLRRLKKEVEAQLPEKVEYVIKCDMSALQRVLYRHMQAKGVLLTDGSEKDKKGKGGTKTLMNTIM
QLRKICNHPYMFQHIEESFSEHLGFTGGIVQGLDLYRASGKFELLDRILPKLRATNHKVLLFCQMTSLMTIMEDYFAYRG
FKYLRLDGTTKAEDRGMLLKTFNEPGSEYFIFLLSTRAGGLGLNLQSADTVIIFDSDWNPHQDLQAQDRAHRIGQQNEVR
VLRLCTVNSVEEKILAAAKYKLNVDQKVIQAGMFDQKSSSHERRAFLQAILEHEEQDEEEDEVPDDETVNQMIARHEEEF
DLFMRMDLDRRREEARNPKRKPRLMEEDELPSWIIKDDAEVERLTCEEEEEKMFGRGSRHRKEVDYSDSLTEKQWLKAIE
EGTLEEIEEEVRQKKSSRKRKRDSDAGSSTPTTSTRSRDKDDESKKQKKRGRPPAEKLSPNPPNLTKKMKKIVDAVIKYK
DSSSGRQLSEVFIQLPSRKELPEYYELIRKPVDFKKIKERIRNHKYRSLNDLEKDVMLLCQNAQTFNLEGSLIYEDSIVL
QSVFTSVRQKIEKEDDSEGEESEEEEEGEEEGSESESRSVKVKIKLGRKEKAQDRLKGGRRRPSRGSRAKPVVSDDDSEE
EQEEDRSGSGSEED
>NR_148052.2
MILSWWLYVHKYIRHLSKLIECIIPRANSNVNYGLWIIMIHQCRFIDCSKCTTLVWDVDSGEAICVGVGGVWELSVLSSQ
FSCESKTALKK
>NR_137288.2
MASSNPPPQPAIGDQLVPGVPGPSSEAEDDPGEAFEFDDSDDEEDTSAALGVPSLAPERDTDPPLIHLDSIPVTDPDPAA
APPGTGVPAWVSNGDAADAAFSGARHSSWKRKSSRRIDRFTFPALEEDVIYDDVPCESPDAHQPGAERNLLYEDAHRAGA
PRQAEDLGWSSSEFESYSEDSGEEAKPEVEVEPAKHRVSFQPKMTQLMKAAKSGTKDGLEKTRMAVMRKVSFLHRKDVLG
DSEEEDMGLLEVSVSDIKPPAPELGPMPEGLSPQQVVRRHILGSIVQSEGSYVESLKRILQDYRNPLMEMEPKALSARKC
QVVFFRVKEILHCHSMFQIALSSRVAEWDSTEKIGDLFVASFSKSMVLDVYSDYVNNFTSAMSIIKKACLTKPAFLEFLK
RRQVCSPDRVTLYGLMVKPIQRFPQFILLLQDMLKNTPRGHPDRLSLQLALTELETLAEKLNEQKRLADQVAEIQQLTKS
VSDRSSLNKLLTSGQRQLLLCETLTETVYGDRGQLIKSKERRVFLLNDMLVCANINFKPANHRGQLEISSLVPLGPKYVV
KWNTALPQVQVVEVGQDGGTYDKDNVLIQHSGAKKASASGQAQNKVYLGPPRLFQELQDLQKDLAVVEQITLLISTLHGT
YQNLNMTVAQDWCLALQRLMRVKEEEIHSANKCRLRLLLPGKPDK
>NR_132740.2
MGDEKDSWKVKTLDEILQEKKRRKEQEEKAEIKRLKNSDDRDSKRDSLEEGELRDHCMEITIRNSPYRREDSMEDRGEED
DSLAIKPPQQMSRKEKVHHRKDEKRKEKCRHHSHSAEGGKHARVKEREHERRKRHREEQDKARREWERQKRREMAREHSR
RERDRLEQLERKRERERKMREQQKEQREQKERERRAEERRKEREARREVSAHHRTMREDYSDKVKASHWSRSPPRPPRER
FELGDGRKPGEARPAPAQKPAQLKEEKMEERDLLSDLQDISDSERKTSSAESSSAESGSGSEEEEEEEEEEEEEGSTSEE
SEEEEEEEEEEEEETGSNSEEASEQSAEEVSEEEMSEDEERENENHLLVVPESRFDRDSGESEEAEEEVGLPERRGVPVP
EQDRGGHLWSGLQSKRQENR
>NR_037687.2
MGTRQKELLDIDSSSVILEDGITKLNTIGHYEISNGSTIKVFKKIANFTSDVEYSDDHCHLILPDSEAFQDVQGKRHRGK
HKFKVKEMYLTKLLSTKVAIHSVLEKLFRSIWSLPNSRAPFAIKYFFDFLDAQAENKKITDPDVVHIWKTNSLPLRFWVN
ILKNPQFVFDIKKTPHIDGCLSVIAQAFMDAFSLTEQQLGKEAPTNKLLYAKDIPTYKEEVKSYYKAIRDLPPLSSSEME
EFLTQESKKHENEFNEEVALTEIYKYIVKYFDEILNKLERERGLEEAQKQLLHVKVLFDEKKKCKWM
>NR_137287.2
MASSNPPPQPAIGDQLVPGVPGPSSEAEDDPGEAFEFDDSDDEEDTSAALGVPSLAPERDTDPPLIHLDSIPVTDPDPAA
APPGTGVPAWVSNGDAADAAFSGARHSSWKRKSSRRIDRFTFPALEEDVIYDDVPCESPDAHQPAGAERNLLYEDAHRAG
APRQAEDLGWSSSEFESYSEDSGEEAKPEVEVEPAKHRVSFQPKLSPDLTRLKERYARTKRDILALRVGGRDMQELKHKY
DCKMTQLMKAAKSGTKDGLEKTRMAVMRKVSFLHRKDVLGDSEEEDMGLLEVSVSDIKPPAPELGPMPEGLSPQQVVRRH
ILGSIVQSEGSYVESLKRILQDYRNPLMEMEPKALSARKCQVVFFRVKEILHCHSMFQIALSSRVAEWDSTEKIGDLFVA
SFSKSMVLDVYSDYVNNFTSAMSIIKKACLTKPAFLEFLKRRQVCSPDRVTLYGLMVKPIQRFPQFILLLQDMLKNTPRG
HPDRLSLQLALTELETLAEKLNEQKRLADQVAEIQQLTKSVSDRSSLNKLLTSGQRQLLLCETLTETVYGDRGQLIKSKE
RRVFLLNDMLVCANINFKPANHRGQLEISSLVPLGPKYVVKWNTALPQVQVVEVGQDGGTYDKDNVLIQHSGAKKASASG
QAQNKVYLGPPRLFQELQDLQKDLAVVEQITLLISTLHGTYQNLNMTVAQDWCLALQRLMRVKEEEIHSANKCRLRLLLP
GKPDK
>NR_157088.2
MADDFGFFSSSESGAPEAAEEDPAAAFLAQQESEIAGIENDEGFGAPAGSHAAPAQPGPTSGAGSEDMGTTVNGDVFQPV
HHQRVQLQTQLPIQPKDEPAHNYSSSIWHSQGQGQKGPAGLRLPTSAQILSPFP
>NR_132739.2
MGDEKDSWKVKTLDEILQEKKRRKEQEEKAEIKRLKNSDDRDSKRDSLEEGELRDHCMEITIRNSPYRREDSMEDRGEED
DSLAIKPPQQMSRKEKVHHRKDEKRKEKCRHHSHSAEGGKHARVKEREHERRKRHREEQDKARREWERQKRREMAREHSR
RERDRLEQLERKRERERKMREQQKEQREQKERERRAEERRKEREARREVSAHHRTMREDYSDKVKASHWSRSPPRPPRER
FELGDGRKPVKEEKMEERDLLSDLQDISDSERKTSSAESSSAESGSGSEEEEEEEEEEEEEGSTSEESEEEEEEEEEEEE
ETGSNSEEASEQSAEEVSEEEMSEDEERENENHLLVVPESRFDRDSGESEEAEEEVGLPERRGVPVPEQDRGGHLWSGLQ
SKRQENR
>NR_045724.2
MADDFGFFSSSESGAPEAAEEDPAAAFLAQQESEIAGIENDEGFGAPAGSHAAPAQPGPTSGAGSEDMGTTVNGDVFQPV
HHQRVQLQTQLPIQPKDEPAHNYSSSIWHSQGQGQKGPAGLRLPTSAQILSPFP
>NR_038863.2
MKSGEDGCPSPKRERICPSLFILLEPLTDWMMPVHIDEGGSSVLSLLLQMLVSSENSLTDPPRNVLPAIWLSLNPVKLTH
KINHHRMLFGFRF
>NR_168349.1
MFGACYKQPLKPSGSEPPAEECRMTPRHAGCDVTEMQRILSQPTFTEHLLRAVCTKLANMYSTSTDCREHCRRGMKAKQL
KAEAGRLTLFADTLYFVWQPYSPLNHLFELFRVMDIVKVRSQMCGNNNAKFKIVVSMEHEGEKHHQGSCQRKGVPIQTPR
EHSWISCKKEFEANP
>NR_168346.1
MFGACYKQPLKPSGSEPPAEECRMTPRHAGCDVTEMQRILSQPTFTEHLLRAVCLVNGKGSLSRPQESILGSLARKNLRR
IHRVSLVMCVRPLSPSKAIISPVTCMYTSRWPEASEESQKK
>NR_168352.1
MFGACYKQPLKPSGSEPPAEECRMTPRHAGCDVTEMQRILSQPTFTEHLLRAVCTKLANMYSTSTDCREHCRRGMKAKQL
KAEAGRSCQRKGVPIQTPREHSWISCKKEFEANP
>NR_168351.1
MFGACYKQPLKPSGSEPPAEECRMTPRHAGCDVTEMQRILSQPTFTEHLLRAVCLVNGKGSLSRPQESILGSLARKNLRR
IHRVSKASYFYIEGCTLTDQTMLSDVCQTSEPKQSHHIPCDLHVYIQMA
>NR_168350.1
MFGACYKQPLKPSGSEPPAEECRMTPRHAGCDVTEMQRILSQPTFTEHLLRAVCTKLANMYSTSTDCREHCRRGMKAKQL
KAEAGRLTLFADTLYFVWQPYSPLNHLFELFRVMDIVKVRSQMCGNNNAKFKIVVSMEHEGEKHHQGSCQRKGVPIQTPR
EHSWISCKKEFEANP
>NR_168347.1
MFGACYKQPLKPSGSEPPAEECRMTPRHAGCDVTEMQRILSQPTFTEHLLRAVCTKLANMYSTSTDCREHCRRGMKAKQL
KAEAGRSCQRKGVPIQTPREHSWISCKKEFEANP
>NR_168348.1
MSSVKAGTGPFHFFCDSSLASGHLDVYMQVTGDMMALLGLRGLTHITKLTLWIRLKFFLARDPRMLSWGLDRDPFPLTRR
HEVDAQ
>NR_123717.2
MPLVEVQLLLLLYTSMRSGLGKKDKEVMTDTQWKPHIVSWQTEERDVGSSASFDCKVPGFCCTFAHAHGWWEERGIAETH
RRGYRVGEKESRRANTPKEQGQLHLVSLRGTETQE
>NR_168381.1
MLHGRRLGAKATLPHPPLWEAPERGPEIVPHSPPGKEARPPWTEATRSPGRKERTHRPPCGGGRTWSPVVSGRGGISLPV
GLQC
>NR_168373.1
MWLQVRPMPRQFCTAWHMALILSLERNVAVGPASHGVKLHLLLLYSGSNLFLILVL
>NR_168385.1
MLRCLGVSGWGRKDQGTHVLRPRRGVPGRRDFRSLPSAGDLGLCRSPPGSSIRAGVLPAAPKVAWGRWGVPEGMEGPCLG
KEGFRCLWGFSAEPGSPEQTRTELPKPDREGALVASGIHVVDRESARSSPPQ
"""
