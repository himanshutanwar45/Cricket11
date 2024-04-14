
let host = process.env.REACT_APP_HOST;

const Get_Team_Data = async (teamType) => {
    try{
        
        const response  = await fetch(`${host}/getTeam/${teamType}`,{mode:'cors'},{
            method:"GET",
            headers:{"Content-Type":"application/json"}
        });
        const data = await response.json()

        return data

    }catch(error){
        throw error
    }
}

const GetPlayerDetails = async (playerId,teamId) => {
    try{
        let host = process.env.REACT_APP_HOST;
        const response  = await fetch(`${host}/getTeam/getTeamPlayer/getTeamPlayerDetail/${playerId}/${teamId}`,{mode:'cors'},{
            method:"GET",
            headers:{"Content-Type":"application/json"}
        });

        const data = await response.json()

        return data

    }catch(error){
        throw error
    }
}

const GetPlayerData = async (teamId) => {
    try{
        const response  = await fetch(`${host}/getTeam/getTeamPlayer/${teamId}`,{mode:'cors'},{
            method:"GET",
            headers:{"Content-Type":"application/json"}
        });

        const data = await response.json()

        return data

    }catch(error){
        throw error
    }
}

const GetTeamName = async (teamId) =>{
    try{
        const response = await fetch(`${host}/getTeam/getTeamName/${teamId}`,{mode:'cors'},{
            method:"GET",
            headers:{"Content-Type":"application/json"}
        })

        const data = await response.json()

        return data
    }catch(error){
        throw error
    }
}


const GetPlayerName = async (playerId,teamId) =>{
    try{
        const response = await fetch(`${host}/getTeam/getPlayerName/${playerId}/${teamId}`,{mode:'cors'},{
            method:"GET",
            headers:{"Content-Type":"application/json"}
        })

        const data = await response.json()

        return data
    }catch(error){
        throw error
    }
}


export {Get_Team_Data, GetPlayerDetails, GetPlayerData, GetTeamName, GetPlayerName};
