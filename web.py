from html.parser import HTMLParser
import requests
import json
import os
import re

from flask import Flask, request
app = Flask(__name__)

answer = {
    "14025135": ['3'],
    "14025136": ['3'],
    "14025137": ['3'],
    "14025138": ['3'],
    "14025139": ['3'],
    "14025140": ['3'],
    "14025141": ['2'],
    "14025142": ['2'],
    "14025143": ['2'],
    "14025144": ['2'],
    "14025145": ['2'],
    "14025146": ['2'],
    "14025147": ['1'],
    "14025148": ['1'],
    "14025149": ['1'],
    "14025150": ['1'],
    "14025151": ['1'],
    "14025152": ['0'],
    "14025153": ['0'],
    "14025154": ['0'],
    "14025155": ['0'],
    "14025156": ['0'],
    "14025157": ['0'],
    "14025158": ['3'],
    "14025159": ['1'],
    "14025160": ['2'],
    "14025161": ['1'],
    "14025162": ['0'],
    "14025163": ['1'],
    "14025164": ['1'],
    "14025165": ['2'],
    "14025166": ['2'],
    "14025167": ['1'],
    "14025168": ['0'],
    "14025169": ['0'],
    "14025170": ['1'],
    "14025171": ['3'],
    "14025172": ['1'],
    "14025173": ['0'],
    "14025174": ['1'],
    "14025175": ['2'],
    "14025176": ['2'],
    "14025177": ['2'],
    "14025178": ['0'],
    "14025179": ['1'],
    "14025180": ['3'],
    "14025181": ['3'],
    "14025182": ['1'],
    "14025183": ['2'],
    "14025184": ['0'],
    "14025185": ['3'],
    "14025186": ['1'],
    "14025187": ['0'],
    "14025188": ['1'],
    "14025189": ['1'],
    "14025190": ['3'],
    "14025191": ['2'],
    "14025192": ['1'],
    "14025193": ['2'],
    "14025194": ['1'],
    "14025195": ['0'],
    "14025196": ['2'],
    "14025197": ['3'],
    "14025198": ['1'],
    "14025199": ['2'],
    "14025200": ['1'],
    "14025201": ['2'],
    "14025202": ['1'],
    "14025203": ['0'],
    "14025204": ['1'],
    "14025205": ['1'],
    "14025206": ['2'],
    "14025207": ['3'],
    "14025208": ['2'],
    "14025209": ['0'],
    "14025210": ['1'],
    "14025211": ['1'],
    "14025212": ['2'],
    "14025213": ['1'],
    "14025214": ['0'],
    "14025215": ['2'],
    "14025216": ['3'],
    "14025217": ['0'],
    "14025218": ['2'],
    "14025219": ['0'],
    "14025220": ['3'],
    "14025221": ['1'],
    "14025222": ['2'],
    "14025223": ['1'],
    "14025224": ['0'],
    "14025225": ['1'],
    "14025226": ['2'],
    "14025227": ['2'],
    "14025228": ['1'],
    "14025229": ['1'],
    "14025230": ['0'],
    "14025231": ['0'],
    "14025232": ['0'],
    "14025233": ['0'],
    "14025234": ['2'],
    "14025235": ['1'],
    "14025236": ['2'],
    "14025237": ['0'],
    "14025238": ['1'],
    "14025239": ['1'],
    "14025241": ['1'],
    "14025242": ['2'],
    "14025243": ['1'],
    "14025244": ['1'],
    "14025245": ['0'],
    "14025246": ['2'],
    "14025247": ['3'],
    "14025248": ['1'],
    "14025249": ['0'],
    "14025250": ['2'],
    "14025251": ['1'],
    "14025252": ['0'],
    "14025253": ['0'],
    "14025254": ['2'],
    "14025255": ['0'],
    "14025256": ['2'],
    "14025257": ['2'],
    "14025258": ['2'],
    "14025259": ['2'],
    "14025260": ['3'],
    "14025261": ['3'],
    "14025262": ['0'],
    "14025263": ['1'],
    "14025264": ['2'],
    "14025265": ['2'],
    "14025266": ['1'],
    "14025267": ['3'],
    "14025268": ['3'],
    "14025269": ['1'],
    "14025270": ['3'],
    "14025271": ['1'],
    "14025272": ['2'],
    "14025273": ['2'],
    "14025274": ['2'],
    "14025275": ['2'],
    "14025276": ['1'],
    "14025277": ['1'],
    "14025278": ['1'],
    "14025279": ['0'],
    "14025280": ['0'],
    "14025293": ['1'],
    "14025294": ['3'],
    "14025299": ['1'],
    "14025300": ['2'],
    "14025301": ['0'],
    "14025302": ['1'],
    "14025303": ['2'],
    "14025304": ['3'],
    "14025305": ['0'],
    "14025306": ['1'],
    "14025307": ['0'],
    "14025308": ['3'],
    "14025309": ['2'],
    "14025310": ['0'],
    "14025311": ['1'],
    "14025312": ['1'],
    "14025313": ['1'],
    "14025314": ['2'],
    "14025315": ['2'],
    "14025316": ['1'],
    "14025317": ['3'],
    "14025318": ['2'],
    "14025319": ['2'],
    "14025320": ['1'],
    "14025321": ['2'],
    "14025322": ['2'],
    "14025323": ['1'],
    "14025324": ['1'],
    "14025325": ['3'],
    "14025326": ['0'],
    "14025327": ['2'],
    "14025328": ['2'],
    "14025329": ['2'],
    "14025330": ['2'],
    "14025331": ['2'],
    "14025332": ['2'],
    "14025333": ['1'],
    "14025334": ['3'],
    "14025335": ['3'],
    "14025336": ['0'],
    "14025337": ['1'],
    "14025338": ['1'],
    "14025339": ['3'],
    "14025340": ['3'],
    "14025341": ['0'],
    "14025342": ['2'],
    "14025343": ['1'],
    "14025344": ['2'],
    "14025345": ['1'],
    "14025346": ['0'],
    "14025347": ['1'],
    "14025348": ['1'],
    "14025349": ['2'],
    "14025350": ['1'],
    "14025351": ['1'],
    "14025352": ['2'],
    "14025353": ['0'],
    "14025354": ['1'],
    "14025355": ['0'],
    "14025356": ['1'],
    "14025357": ['3'],
    "14025358": ['1'],
    "14025359": ['3'],
    "14025360": ['3'],
    "14025361": ['0'],
    "14025362": ['2'],
    "14025363": ['3'],
    "14025364": ['0'],
    "14025365": ['2'],
    "14025366": ['1'],
    "14025367": ['0'],
    "14025368": ['3'],
    "14025369": ['2'],
    "14025370": ['3'],
    "14025371": ['1'],
    "14025372": ['0'],
    "14025373": ['0'],
    "14025374": ['0'],
    "14025375": ['0'],
    "14025376": ['0'],
    "14025377": ['0'],
    "14025378": ['0'],
    "14025379": ['0'],
    "14025380": ['0'],
    "14025381": ['0'],
    "14025382": ['2'],
    "14025383": ['1'],
    "14025384": ['0'],
    "14025385": ['0'],
    "14025386": ['1'],
    "14025387": ['0'],
    "14025388": ['0'],
    "14025389": ['3'],
    "14025390": ['1'],
    "14025391": ['0'],
    "14025392": ['1'],
    "14025393": ['3'],
    "14025394": ['0'],
    "14025395": ['3'],
    "14025396": ['0'],
    "14025397": ['1'],
    "14025398": ['0'],
    "14025399": ['3'],
    "14025400": ['2'],
    "14025401": ['2'],
    "14025402": ['0'],
    "14025404": ['0'],
    "14025405": ['0'],
    "14025406": ['0'],
    "14025407": ['0'],
    "14025408": ['0'],
    "14025409": ['0'],
    "14025410": ['0'],
    "14025411": ['0'],
    "14025412": ['0'],
    "14025413": ['0'],
    "14025414": ['0'],
    "14025415": ['0'],
    "14025416": ['0'],
    "14025417": ['0'],
    "14025418": ['0'],
    "14025419": ['0'],
    "14025420": ['0'],
    "14025421": ['0'],
    "14025422": ['0'],
    "14025423": ['0'],
    "14025424": ['0'],
    "14025425": ['0'],
    "14025426": ['0'],
    "14025427": ['0'],
    "14025428": ['0'],
    "14025429": ['0'],
    "14025430": ['0'],
    "14025431": ['0'],
    "14025432": ['0'],
    "14025433": ['0'],
    "14025434": ['0'],
    "14025435": ['0'],
    "14025436": ['0'],
    "14025437": ['0'],
    "14025438": ['0'],
    "14025439": ['0'],
    "14025440": ['0'],
    "14025441": ['0'],
    "14025442": ['0'],
    "14025443": ['0'],
    "14025444": ['0'],
    "14025445": ['0'],
    "14025446": ['0'],
    "14025447": ['0'],
    "14025448": ['0'],
    "14025449": ['0'],
    "14025450": ['0'],
    "14025451": ['0'],
    "14025452": ['0'],
    "14025453": ['0'],
    "14025454": ['0'],
    "14025455": ['0'],
    "14025456": ['0'],
    "14025457": ['3', '1'],
    "14025458": ['3', '1', '2'],
    "14025459": ['3', '2', '1'],
    "14025460": ['2', '0', '3'],
    "14025461": ['0', '3', '2'],
    "14025462": ['0', '2'],
    "14025463": ['1', '3', '0'],
    "14025464": ['4', '1', '0', '5', '2', '3'],
    "14025465": ['0', '3', '4', '2', '5', '1'],
    "14025466": ['4', '2', '0', '3', '1'],
    "14025467": ['2', '3', '0', '1'],
    "14025468": ['2', '3', '0', '1'],
    "14025469": ['0', '2', '1'],
    "14025470": ['0', '2', '1'],
    "14025471": ['1', '0', '2'],
    "14025472": ['1', '0'],
    "14025473": ['0', '1'],
    "14025474": ['1', '0', '2', '3'],
    "14025475": ['0', '3', '2', '1'],
    "14025476": ['1', '0'],
    "14025477": ['0', '1'],
    "14025478": ['1', '3', '0', '2'],
    "14025479": ['2', '4', '3', '0', '1'],
    "14025480": ['3', '0', '2', '1'],
    "14025481": ['1', '2'],
    "14025482": ['0', '2', '1'],
    "14025483": ['2', '0', '3', '1'],
    "14025484": ['0', '2', '1'],
    "14025485": ['3', '1', '2'],
    "14025486": ['2', '4', '3', '0', '1'],
    "14025487": ['0', '2', '1'],
    "14025488": ['2', '1'],
    "14025489": ['0', '1'],
    "14025490": ['3', '2', '0', '1'],
    "14025491": ['3', '2', '0'],
    "14025492": ['1', '0', '2'],
    "14025493": ['0', '3'],
    "14025494": ['0', '1'],
    "14025495": ['0', '1', '3'],
    "14025496": ['2', '0'],
    "14025497": ['2'],
    "14025498": ['2', '1', '0'],
    "14025499": ['2', '0', '1', '3'],
    "14025500": ['0', '2', '1'],
    "14025501": ['1', '0', '2', '3'],
    "14025502": ['0', '3', '2'],
    "14025503": ['1', '0'],
    "14025504": ['0', '3'],
    "14025505": ['0', '2', '1', '3', '4'],
    "14025506": ['0', '2'],
    "14025507": ['0', '1'],
    "14025508": ['0', '1', '2'],
    "14025509": ['1', '3', '2'],
    "14025510": ['0', '3', '1'],
    "14025511": ['2', '0'],
    "14025512": ['2', '1', '0', '3'],
    "14025513": ['2', '0', '1'],
    "14025514": ['2', '1', '4', '3', '0'],
    "14025515": ['0', '2', '1'],
    "14025516": ['2', '0', '3'],
    "14025517": ['3', '0', '2'],
    "14025518": ['2', '1', '4'],
    "14025519": ['1', '2'],
    "14025520": ['0', '2', '3'],
    "14025521": ['2', '0'],
    "14025522": ['2', '3'],
    "14025523": ['2', '0'],
    "14025524": ['0', '1'],
    "14025525": ['0', '3'],
    "14025526": ['1', '3', '0', '2'],
    "14025527": ['2', '0', '1'],
    "14025528": ['0', '2'],
    "14025529": ['2', '0', '1'],
    "14025530": ['1', '0'],
    "14025531": ['0', '2'],
    "14025532": ['1', '0'],
    "14025533": ['2', '1', '0'],
    "14025534": ['1', '2', '3'],
    "14025535": ['3', '0', '1'],
    "14025536": ['2', '0', '1'],
    "14025537": ['3', '2', '1'],
    "14025538": ['0', '2', '1', '3'],
    "14025539": ['0', '1'],
    "14025540": ['1', '0'],
    "14025541": ['0', '3', '1', '2'],
    "14025542": ['3', '0'],
    "14025543": ['0', '1'],
    "14025544": ['2', '1'],
    "14025545": ['2', '3'],
    "14025546": ['3', '2'],
    "14025547": ['3', '0', '2'],
    "14025548": ['2', '0', '4', '3', '1'],
    "14025549": ['2', '3', '4', '0', '5', '1'],
    "14025550": ['2', '0', '1', '3'],
    "14025551": ['1', '4', '3', '2', '0'],
    "14025552": ['0', '1', '2'],
    "14025553": ['0', '1', '2'],
    "14025554": ['1', '0', '2', '3'],
    "14025555": ['2', '3', '0', '1'],
    "14025556": ['2', '1', '0'],
    "14025557": ['0', '2', '1'],
    "14025558": ['0', '1'],
    "14025559": ['3', '2', '0', '1'],
    "14025560": ['0', '3', '1', '2'],
    "14025561": ['0', '2', '1', '3'],
    "14025562": ['0', '2', '1'],
    "14025563": ['3', '2', '0', '1'],
    "14025564": ['2', '0', '1', '3'],
    "14025565": ['0', '1', '2'],
    "14025566": ['3', '0', '2', '1'],
    "14025567": ['0', '2', '1', '3'],
    "14025568": ['0', '2', '1'],
    "14025569": ['3', '2', '0', '1'],
    "14025570": ['1', '0', '3'],
    "14025571": ['0'],
    "14025572": ['0'],
    "14025573": ['0'],
    "14025574": ['0'],
    "14025575": ['0'],
    "14025576": ['0'],
    "14025577": ['0'],
    "14025578": ['0'],
    "14025579": ['0'],
    "14025580": ['0'],
    "14025581": ['0'],
    "14025582": ['0'],
    "14025583": ['0'],
    "14025584": ['0'],
    "14025585": ['0'],
    "14025586": ['0'],
    "14025587": ['0'],
    "14025588": ['0'],
    "14025589": ['0'],
    "14025590": ['0'],
    "14025591": ['0'],
    "14025592": ['0'],
    "14025593": ['0'],
    "14025594": ['0'],
    "14025595": ['0'],
    "14025596": ['0'],
    "14025597": ['0'],
    "14025598": ['0'],
    "14025599": ['0'],
    "14025600": ['0'],
    "14025601": ['0'],
    "14025602": ['0'],
    "14025603": ['0'],
    "14025604": ['0'],
    "14025605": ['0'],
    "14025606": ['0'],
    "14025607": ['0'],
    "14025608": ['0'],
    "14025609": ['0'],
    "14025610": ['1'],
    "14025611": ['1'],
    "14025612": ['1'],
    "14025613": ['1'],
    "14025614": ['1'],
    "14025615": ['1'],
    "14025616": ['1'],
    "14025617": ['1'],
    "14025618": ['1'],
    "14025619": ['1'],
    "14025620": ['1'],
    "14025621": ['1'],
    "14025622": ['1'],
    "14025623": ['1'],
    "14025624": ['1'],
    "14025625": ['1'],
    "14025626": ['1'],
    "14025627": ['1'],
    "14025628": ['1'],
    "14025629": ['1'],
    "14025630": ['1'],
    "14025631": ['1'],
    "14025632": ['1'],
    "14025633": ['1'],
    "14025634": ['0'],
    "14025635": ['0'],
    "14025636": ['0'],
    "14025637": ['0'],
    "14025638": ['0'],
    "14025639": ['0'],
    "14025640": ['0'],
    "14025641": ['0'],
    "14025642": ['0'],
    "14025643": ['0'],
    "14025644": ['0'],
    "14025645": ['0'],
    "14025646": ['0'],
    "14025647": ['0'],
    "14025648": ['0'],
    "14025649": ['0'],
    "14025650": ['0'],
    "14025651": ['0'],
    "14025652": ['0'],
    "14025653": ['0'],
    "14025654": ['0'],
    "14025655": ['0'],
    "14025656": ['0'],
    "14025657": ['0'],
    "14025658": ['0'],
    "14025659": ['0'],
    "14025660": ['0'],
    "14025661": ['0'],
    "14025662": ['0'],
    "14025663": ['0'],
    "14025664": ['1'],
    "14025665": ['0'],
    "14025666": ['0'],
    "14025667": ['0'],
    "14025668": ['0'],
    "14025669": ['0'],
    "14025670": ['0'],
    "14025671": ['0'],
    "14025672": ['0'],
    "14025673": ['0'],
    "14025674": ['0'],
    "14025675": ['0'],
    "14025676": ['0'],
    "14025677": ['0'],
    "14025678": ['0'],
    "14025679": ['0'],
    "14025680": ['0'],
    "14025681": ['0'],
    "14025682": ['0'],
    "14025683": ['0'],
    "14025684": ['0'],
    "14025685": ['0'],
    "14025686": ['0'],
    "14025687": ['0'],
    "14025688": ['0'],
    "14025689": ['0'],
    "14025690": ['0'],
    "14025691": ['1'],
    "14025692": ['0'],
    "14025693": ['0'],
    "14025694": ['0'],
    "14025695": ['0'],
    "14025696": ['0'],
    "14025697": ['0'],
    "14025698": ['0'],
    "14025699": ['1'],
    "14025700": ['0'],
    "14025701": ['0'],
    "14025702": ['0'],
    "14025703": ['1'],
    "14025704": ['0'],
    "14025705": ['1'],
    "14025706": ['0'],
    "14025707": ['0'],
    "14025708": ['0'],
    "14025709": ['1'],
    "14025710": ['0'],
    "14025711": ['0'],
    "14025712": ['0'],
    "14025713": ['0'],
    "14025714": ['0'],
    "14025715": ['0'],
    "14025716": ['0'],
    "14025717": ['1'],
    "14025718": ['0'],
    "14025719": ['0'],
    "14025720": ['0'],
    "14025721": ['0'],
    "14025722": ['0'],
    "14025723": ['0'],
    "14025724": ['0'],
    "14025725": ['1'],
    "14025726": ['0'],
    "14025727": ['1'],
    "14025728": ['1'],
    "14025729": ['0'],
    "14025730": ['0'],
    "14025731": ['0'],
    "14025732": ['1'],
    "14025733": ['1'],
    "14025734": ['0'],
    "14025735": ['1'],
    "14025736": ['1'],
    "14025737": ['0'],
    "14025738": ['0'],
    "14025739": ['1'],
    "14025740": ['1'],
    "14025741": ['0'],
    "14025742": ['1'],
    "14025743": ['0'],
    "14025744": ['1'],
    "14025745": ['1'],
    "14025746": ['0'],
    "14025747": ['1'],
    "14025748": ['1'],
    "14025749": ['1'],
    "14025750": ['0'],
    "14025751": ['0'],
    "14025752": ['0'],
    "14025753": ['0'],
    "14025754": ['1'],
    "14025755": ['0'],
    "14025756": ['0'],
    "14025757": ['0'],
    "14025758": ['0'],
    "14025759": ['1'],
    "14025760": ['1'],
    "14025761": ['1'],
    "14025762": ['1'],
    "14025763": ['0'],
    "14025764": ['1'],
    "14025765": ['0'],
    "14025766": ['1'],
    "14025767": ['0'],
    "14025768": ['0'],
    "14025769": ['1'],
    "14025770": ['1'],
    "14025771": ['1'],
    "14025772": ['1'],
    "14025773": ['0'],
    "14025774": ['1'],
    "14025775": ['0'],
    "14025776": ['1'],
    "14025777": ['1'],
    "14025778": ['1'],
    "14025779": ['0'],
    "14025780": ['1'],
    "14025781": ['0'],
    "14025782": ['1'],
    "14025783": ['1'],
    "14025784": ['0'],
    "14025785": ['0'],
    "14025786": ['1'],
    "14025787": ['0'],
    "14025788": ['1'],
    "14025789": ['0'],
    "14025790": ['1'],
    "14025791": ['1'],
    "14025792": ['1'],
    "14025793": ['0'],
    "14025794": ['0'],
    "14025795": ['1'],
    "14025796": ['1'],
    "14025797": ['0'],
    "14025798": ['0'],
    "14025799": ['0'],
    "14025800": ['1'],
    "14025801": ['1'],
    "14025802": ['1'],
    "14025803": ['1'],
    "14025804": ['0'],
    "14025805": ['0'],
    "14025806": ['0'],
    "14025807": ['1'],
    "14025808": ['1'],
    "14025809": ['0'],
    "14025810": ['0'],
    "14025811": ['0'],
    "14025812": ['0'],
    "14025813": ['0'],
    "14025814": ['1'],
    "14025815": ['0'],
    "14025816": ['0'],
    "14025817": ['1'],
    "14025818": ['1'],
    "14025819": ['1'],
    "14025820": ['0'],
    "14025821": ['0'],
    "14025822": ['0'],
    "14025823": ['0'],
    "14025824": ['0'],
    "14025825": ['0'],
    "14025826": ['1'],
    "14025827": ['1'],
    "14025828": ['1'],
    "14025829": ['0'],
    "14025830": ['0'],
    "14025831": ['0'],
    "14025832": ['0'],
    "14025833": ['0'],
    "14025834": ['0'],
    "14025835": ['0'],
    "14025836": ['0'],
    "14025837": ['0'],
    "14025838": ['0'],
    "14025839": ['0'],
    "14025840": ['0'],
    "14025841": ['0'],
    "14025842": ['0'],
    "14025843": ['0'],
    "14025844": ['0'],
    "14025845": ['0'],
    "14025846": ['0'],
    "14025847": ['0'],
    "14025848": ['0'],
    "14025849": ['0'],
    "14025850": ['0'],
    "14025851": ['0'],
    "14025852": ['0'],
    "14025853": ['0'],
    "14025854": ['0'],
    "14025855": ['1'],
    "14025856": ['0'],
    "14025857": ['0'],
    "14025858": ['0'],
    "14025859": ['0'],
    "14025860": ['0'],
    "14025861": ['0'],
    "14025862": ['0'],
    "14025863": ['0'],
    "14025864": ['0'],
    "14025865": ['0'],
    "14025866": ['0'],
    "14025867": ['0'],
    "14025868": ['0'],
    "14025869": ['2', '1'],
    "14025870": ['2', '1'],
    "14025871": ['2', '1'],
    "14025872": ['0', '3', '2', '4', '5'],
    "14025873": ['0', '2', '3'],
    "14025874": ['0', '3', '2', '1', '4'],
    "14025875": ['2', '3', '0', '1'],
    "14025876": ['0', '3', '1', '2'],
    "14025877": ['1', '3', '0', '2'],
    "14025878": ['0', '2', '3', '1'],
    "14025879": ['1', '0', '2', '3'],
    "14025880": ['1', '2', '0'],
    "14025881": ['0', '2', '1'],
    "14025882": ['0', '2', '1'],
    "14025883": ['0', '1'],
    "14025884": ['1', '4', '3', '2', '0'],
    "14025885": ['2', '0'],
    "14025886": ['0'],
    "14025887": ['0', '1'],
    "14025888": ['0', '4', '3', '5'],
    "14025889": ['4', '0', '2', '3', '1', '5'],
    "14025890": ['3', '0'],
    "14025891": ['2', '3', '1', '5'],
    "14025892": ['3', '0', '1', '2'],
    "14025893": ['4'],
    "14025894": ['4'],
    "14025895": ['3'],
    "14025896": ['3', '0', '2', '1', '5', '4'],
    "14025897": ['2', '3', '0', '1'],
    "14025898": ['2', '0', '3', '1']
}

class QuestionPage(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.question_id_array = []
 
    def handle_starttag(self, tag, attrs):
        if tag == "div":
            for (variable, value) in attrs:
                if variable == "id":
                    if "question-" in value:
                        self.question_id_array.append(value[-8:])



def GetCookies():
    login_url = "https://www.yooc.me/login"
    response = requests.get(login_url)
    return_cookie = {}
    for key,value in response.cookies.items():  
        return_cookie[key] = value 
    return return_cookie



def Login(form_data, cookies):
    login_url = "https://www.yooc.me/yiban_account/login_ajax"
    request_headers = {"X-CSRFToken": cookies["csrftoken"]}
    response = requests.post(login_url, data = form_data, headers = request_headers, cookies = cookies)
    return_cookie = {}
    for key,value in response.cookies.items():  
        return_cookie[key] = value 
    return return_cookie



def RepeatExam(cookies):
    exam_url = "https://www.yooc.me/group/39666/exams"
    repeat_url = re.compile("repeat-url=\"(.*?)\"").findall(requests.get(exam_url, cookies = cookies).text)[0]
    request_headers = {"X-CSRFToken": cookies["csrftoken"], "Cookie": "csrftoken=" + cookies["csrftoken"] + "; sessionid=" + cookies["sessionid"]}
    form_data = {"csrfmiddlewaretoken": cookies["csrftoken"]}
    response = requests.post(repeat_url, headers = request_headers, data = form_data, cookies = cookies)



def SubmitAnswer(cookies, answers):
    submit_url = "https://www.yooc.me/group/39666/exam/77777/answer/submit"
    request_headers = {"X-CSRFToken": cookies["csrftoken"], "Cookie": "csrftoken=" + cookies["csrftoken"] + "; sessionid=" + cookies["sessionid"]}
    form_data = {"csrfmiddlewaretoken": cookies["csrftoken"], "answers": json.dumps(answers), "completed": "1", "auto": "0"}
    response = requests.post(submit_url, headers = request_headers, data = form_data, cookies = cookies)



def GetExamPage(cookies):
    exam_url = "https://www.yooc.me/group/39666/exam/77777/detail"
    return requests.get(exam_url, cookies = cookies).text



def ParseQuestion(page):
    parser = QuestionPage()
    parser.feed(page)
    return parser.question_id_array



def BuildAnswer(question_id_array):
    answers = []
    for question_id in question_id_array:
        answer_chunk = {}
        answer_chunk[question_id] = {}
        answer_chunk[question_id]["1"] = answer.get(question_id, [0])
        answers.append(answer_chunk)
    return answers



@app.route('/')
def PrintHtml():
    email = request.args.get("email")
    password = request.args.get("password")
    if (email == None or email == "" or password == None or password == ""):
        return "手机号/密码不能为空！"
    cookies = GetCookies()
    form_data = {"email": email, "password": password, "remember": True}
    cookies = Login(form_data, cookies)
    RepeatExam(cookies)
    page = GetExamPage(cookies)
    question_id_array = ParseQuestion(page)
    answers = BuildAnswer(question_id_array)
    SubmitAnswer(cookies, answers)
    return "已完成！"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5001)