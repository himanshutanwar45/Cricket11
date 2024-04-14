
from flask import Flask,jsonify,request,json,session
from Classes.Working.DatabaseCall.TeamModule.GetTeam import GetTeam
from Classes.Working.DatabaseCall.MatchList.GetMatchList import GetMatchList
from Classes.Working.APICall.TeamModule.APITeamModule import APITeamModules
from Classes.Working.DatabaseCall.Login.Login import LoginDetails
from flask_cors import CORS

app = Flask("__name__")
app.secret_key="qwr@#$%*(hif5768t#$%*jlwifjslac5768tfdey465768t4786&$*&(rhefbiu2eo rc97y25orhj)"
CORS(app, origins="*")

@app.route('/session/close',methods=['GET','POST'])
def Home():
    session.clear()
    return jsonify ({'session':session})

##############Start the login Process ################################################
#Login users
@app.route("/api/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        json_string = json.dumps(data)
        response = ""
        authToken,data_list = LoginDetails.LoginUser(json_string)
        if authToken!="":
            session['User_Code'] = data_list[0].get('User_Code')  
            session['auth-Token'] = authToken
            response = jsonify({'success':True,'message': authToken, 'data_list': data_list})
        else:
            response = jsonify({'success':False,'message': authToken})
            
        response.headers['auth-Token'] = authToken
        return response
    except Exception as ex:
        return jsonify({'success':False,'message':str(ex)})
    

#Login Name 
@app.route("/api/loginName", methods=["GET"])
def loginName():
    try:
        User_Code = session.get('User_Code')
        authToken = session.get('authToken')
        data = LoginDetails.LoginDetails(User_Code)
        response = jsonify({'success':True,'message':data})
        response.headers['auth-Token'] = authToken
        return response
    except Exception as ex:
        return jsonify({'success':False,'message':str(ex)})

#################################      END      ########################################

################Start Team List Module##############################################

@app.route('/api/getTeam/<string:TeamType>',methods=['GET'])
def getTeam(TeamType):
    usage_data = GetTeam.GetTeamDetails(TeamType)
    return jsonify(usage_data)


@app.route('/api/getTeam/getTeamPlayer/<int:TeamId>', methods=['GET'])
def getTeamPlayer(TeamId):
    usage_data = GetTeam.GetTeamPlayerDetails(TeamId)
    return jsonify(usage_data)

@app.route('/api/getTeam/getTeamName/<int:TeamId>', methods=['GET'])
def getTeamName(TeamId):
    usage_data = GetTeam.GetTeamName(TeamId)
    return jsonify(usage_data)

@app.route('/api/getTeam/getPlayerName/<int:PlayerId>/<int:TeamId>', methods=['GET'])
def getPlayerName(PlayerId,TeamId):
    usage_data = GetTeam.GetPlayerName(PlayerId,TeamId)
    return jsonify(usage_data)

@app.route('/api/getTeam/getTeamPlayer/getTeamPlayerDetail/<int:PlayerId>/<int:TeamId>', methods=['GET'])
def getTeamPlayerDetail(PlayerId,TeamId):
    usage_data = GetTeam.GetTeamPlayerInfo(PlayerId,TeamId)
    return jsonify(usage_data)

@app.route("/api/getTeam/APIGetTeam/<string:User_Code>", methods=["GET"])
def APIGetTeam(User_Code):
    try:
        data = APITeamModules.APIGetTeamList(User_Code)  
        response = jsonify({'success':True,'message':data})    
        return response
    except Exception as ex:
        return jsonify({'success':False,'message':'Catch :' + str(ex)})
    
@app.route("/api/getTeam/APIGetPlayerTeamId/<int:TeamId>/<string:User_Code>", methods=["GET"])
def APIGetPlayerTeamId(User_Code,TeamId):
    try:
        data = APITeamModules.APIGetPlayerByTeamId(User_Code,TeamId)
        response = jsonify({'success':True,'message':data})
        return response
    except Exception as ex:
        return jsonify({'success':False,'message':str(ex)})
    

@app.route("/api/getTeam/APIGetPlayerInfoPlayerInfo/<int:Player_Id>/<string:User_Code>", methods=["GET"])
def APIGetPlayerInfoPlayerInfo(User_Code,Player_Id):
    try:
        data = APITeamModules.APIGetPlayerInfoByPlayerId(User_Code,Player_Id)
        response = jsonify({'success':True,'message':data})
        return response
    except Exception as ex:
        return jsonify({'success':False,'message':str(ex)})
    
#######################         END             #################################################

####################### Start Recent Match List   #################################################

@app.route("/api/getMatchType", methods=["GET"])
def getMatch():
    try:
        data = GetMatchList.GetMatchType()
        response = jsonify(data)
        return response
    except Exception as ex:
        return jsonify(str(ex))
    


@app.route("/api/getMatchList/<string:MatchType>", methods=["GET"])
def getMatchList(MatchType):
    try:
        data = GetMatchList.GetRecentmatchList(MatchType)
        response = jsonify(data)
        return response
    except Exception as ex:
        return jsonify(str(ex))
    

@app.route("/api/getMatchList/GetScore/<int:MatchId>", methods=["GET"])
def GetScore(MatchId):
    try:
        data = GetMatchList.GetMatchListScore(MatchId)
        response = jsonify(data)
        return response
    except Exception as ex:
        return jsonify(str(ex))
    

@app.route("/api/getMatchList/GetScore/GetScoreBatter/<int:MatchId>/<int:TeamId>", methods=["GET"])
def GetScoreBatter(MatchId,TeamId):
    try:
        data = GetMatchList.GetBatterDetails(MatchId,TeamId)
        response = jsonify(data)
        return response
    except Exception as ex:
        return jsonify(str(ex))
    

@app.route("/api/getMatchList/GetScore/GetScoreBowler/<int:MatchId>/<int:TeamId>", methods=["GET"])
def GetScoreBowler(MatchId,TeamId):
    try:
        data = GetMatchList.GetBowlerDetails(MatchId,TeamId)
        response = jsonify(data)
        return response
    except Exception as ex:
        return jsonify(str(ex))
#######################         END             #################################################
  
if __name__ == '__main__':
    app.run(debug=True) 