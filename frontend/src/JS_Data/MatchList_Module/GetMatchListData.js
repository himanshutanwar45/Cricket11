
let host = process.env.REACT_APP_HOST;

const Get_Match_Type = async () => {
    try{
        
        const response  = await fetch(`${host}/getMatchType`,{mode:'cors'},{
            method:"GET",
            headers:{"Content-Type":"application/json"}
        });
        const data = await response.json()

        return data

    }catch(error){
        throw error
    }
}

const Get_Recent_Match = async  (matchType) => {
    try{
        
        const response  = await fetch(`${host}/getMatchList/${matchType}`,{mode:'cors'},{
            method:"GET",
            headers:{"Content-Type":"application/json"}
        });
        const data = await response.json()

        return data

    }catch(error){
        throw error
    }
}


const Get_Recent_Match_Score = async  (matchId) => {
    try{
        
        const response  = await fetch(`${host}/getMatchList/GetScore/${matchId}`,{mode:'cors'},{
            method:"GET",
            headers:{"Content-Type":"application/json"}
        });
        const data = await response.json()

        return data

    }catch(error){
        throw error
    }
}


const Get_Recent_Match_Score_Batter = async  (matchId,teamId) => {
    try{
        
        const response  = await fetch(`${host}/getMatchList/GetScore/GetScoreBatter/${matchId}/${teamId}`,{mode:'cors'},{
            method:"GET",
            headers:{"Content-Type":"application/json"}
        });
        const data = await response.json()

        return data

    }catch(error){
        throw error
    }
}


const Get_Recent_Match_Score_Bowler = async  (matchId,teamId) => {
    try{
        
        const response  = await fetch(`${host}/getMatchList/GetScore/GetScoreBowler/${matchId}/${teamId}`,{mode:'cors'},{
            method:"GET",
            headers:{"Content-Type":"application/json"}
        });
        const data = await response.json()

        return data

    }catch(error){
        throw error
    }
}

export {Get_Match_Type, Get_Recent_Match, Get_Recent_Match_Score, Get_Recent_Match_Score_Batter, Get_Recent_Match_Score_Bowler}