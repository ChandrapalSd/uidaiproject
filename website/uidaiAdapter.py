from subprocess import PIPE, run
import json, xmltodict
from typing import List
# TODO Update path according to system

def genUidaiOtp(uid :str = "") -> dict:
    if len(uid)<12:
        d = {'result':'n','txnId':'','err':'Invalid uid'}
        return d
    # if uid=='999999021756':
    #     d = {'result':'y','txnId':'test','err':'null'}
        return d
    exePath = "/home/chandrapalsd/.jdks/corretto-1.8.0_312/bin/java -javaagent:/webresource/apps/idea-IC-212.5457.46/lib/idea_rt.jar=42403:/webresource/apps/idea-IC-212.5457.46/bin -Dfile.encoding=UTF-8 -classpath /home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/charsets.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/cldrdata.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/dnsns.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/jaccess.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/jfxrt.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/localedata.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/nashorn.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/sunec.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/sunjce_provider.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/sunpkcs11.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/zipfs.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/jce.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/jfr.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/jfxswt.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/jsse.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/management-agent.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/resources.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/rt.jar:/webresource/apps/otpapiclient-master/target/classes:/home/chandrapalsd/.m2/repository/com/sun/jersey/jersey-client/1.9.1/jersey-client-1.9.1.jar:/home/chandrapalsd/.m2/repository/com/sun/jersey/jersey-core/1.9.1/jersey-core-1.9.1.jar:/home/chandrapalsd/.m2/repository/org/bouncycastle/bcprov-jdk16/1.46/bcprov-jdk16-1.46.jar in.gov.uidai.otpapiclient.OtpAPIClientMain "
    return json.loads(run(exePath+uid, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True).stdout)

def ekycName(uid:str,txnId:str, otp):
    if len(uid)<12:
        return {'status':'n'}
    exePath = f"/home/chandrapalsd/.jdks/corretto-1.8.0_312/bin/java -javaagent:/webresource/apps/idea-IC-212.5457.46/lib/idea_rt.jar=38833:/webresource/apps/idea-IC-212.5457.46/bin -Dfile.encoding=UTF-8 -classpath /home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/charsets.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/cldrdata.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/dnsns.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/jaccess.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/jfxrt.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/localedata.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/nashorn.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/sunec.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/sunjce_provider.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/sunpkcs11.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/zipfs.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/jce.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/jfr.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/jfxswt.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/jsse.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/management-agent.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/resources.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/rt.jar:/webresource/apps/ekycapiclient-master/target/classes:/home/chandrapalsd/.m2/repository/commons-io/commons-io/1.3.2/commons-io-1.3.2.jar:/home/chandrapalsd/.m2/repository/com/sun/jersey/jersey-client/1.9.1/jersey-client-1.9.1.jar:/home/chandrapalsd/.m2/repository/com/sun/jersey/jersey-core/1.9.1/jersey-core-1.9.1.jar:/home/chandrapalsd/.m2/repository/commons-codec/commons-codec/1.13/commons-codec-1.13.jar:/home/chandrapalsd/.m2/repository/commons-lang/commons-lang/2.6/commons-lang-2.6.jar:/home/chandrapalsd/.m2/repository/org/bouncycastle/bcprov-jdk16/1.46/bcprov-jdk16-1.46.jar:/home/chandrapalsd/.m2/repository/castor/castor/0.9.7/castor-0.9.7.jar:/home/chandrapalsd/.m2/repository/xerces/xercesImpl/2.8.1/xercesImpl-2.8.1.jar:/home/chandrapalsd/.m2/repository/xml-apis/xml-apis/1.3.03/xml-apis-1.3.03.jar:/home/chandrapalsd/.m2/repository/commons-logging/commons-logging/1.2/commons-logging-1.2.jar:/home/chandrapalsd/.m2/repository/oro/oro/2.0.8/oro-2.0.8.jar main.Main {uid} {txnId} {otp}"
    res = run(exePath, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True).stdout
    if(res.strip() == 'n' or not res.strip()):
        return {'status':'n'}
    res = json.loads(json.dumps(xmltodict.parse(res)))

    return {'status':'y', 'name':res['KycRes']['UidData']['Poi']['@name']}
    
def ekycAddr(uid:str,txnId:str, otp):
    if len(uid)<12:
        return {'status':'n'}
    exePath = f"/home/chandrapalsd/.jdks/corretto-1.8.0_312/bin/java -javaagent:/webresource/apps/idea-IC-212.5457.46/lib/idea_rt.jar=38833:/webresource/apps/idea-IC-212.5457.46/bin -Dfile.encoding=UTF-8 -classpath /home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/charsets.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/cldrdata.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/dnsns.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/jaccess.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/jfxrt.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/localedata.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/nashorn.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/sunec.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/sunjce_provider.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/sunpkcs11.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/ext/zipfs.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/jce.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/jfr.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/jfxswt.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/jsse.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/management-agent.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/resources.jar:/home/chandrapalsd/.jdks/corretto-1.8.0_312/jre/lib/rt.jar:/webresource/apps/ekycapiclient-master/target/classes:/home/chandrapalsd/.m2/repository/commons-io/commons-io/1.3.2/commons-io-1.3.2.jar:/home/chandrapalsd/.m2/repository/com/sun/jersey/jersey-client/1.9.1/jersey-client-1.9.1.jar:/home/chandrapalsd/.m2/repository/com/sun/jersey/jersey-core/1.9.1/jersey-core-1.9.1.jar:/home/chandrapalsd/.m2/repository/commons-codec/commons-codec/1.13/commons-codec-1.13.jar:/home/chandrapalsd/.m2/repository/commons-lang/commons-lang/2.6/commons-lang-2.6.jar:/home/chandrapalsd/.m2/repository/org/bouncycastle/bcprov-jdk16/1.46/bcprov-jdk16-1.46.jar:/home/chandrapalsd/.m2/repository/castor/castor/0.9.7/castor-0.9.7.jar:/home/chandrapalsd/.m2/repository/xerces/xercesImpl/2.8.1/xercesImpl-2.8.1.jar:/home/chandrapalsd/.m2/repository/xml-apis/xml-apis/1.3.03/xml-apis-1.3.03.jar:/home/chandrapalsd/.m2/repository/commons-logging/commons-logging/1.2/commons-logging-1.2.jar:/home/chandrapalsd/.m2/repository/oro/oro/2.0.8/oro-2.0.8.jar main.Main {uid} {txnId} {otp}"
    res = run(exePath, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True).stdout
    if(res.strip() == 'N' or not res.strip()):
        return {'status':'n'}

    res = json.loads(json.dumps(xmltodict.parse(res)))


    return { 'status':'y',
             'address': res['KycRes']['UidData']['Poa']['@loc']+" "+
                        res['KycRes']['UidData']['Poa']['@vtc']+" "+
                        res['KycRes']['UidData']['Poa']['@dist']+" "+
                        res['KycRes']['UidData']['Poa']['@state']+" "+
                        res['KycRes']['UidData']['Poa']['@country']+" "+
                        res['KycRes']['UidData']['Poa']['@pc']
        }