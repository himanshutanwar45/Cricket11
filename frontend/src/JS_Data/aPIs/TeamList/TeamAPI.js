
let host = process.env.REACT_APP_HOST;
let token = localStorage ? localStorage.getItem('auth-Token'):null;
let User_Code = localStorage ? localStorage.getItem('User_Code'):null

const Get_Team_Data_API = async () =>{
    try{
        const response = await fetch(`${host}/getTeam/APIGetTeam/${User_Code}`,{mode:'cors'},{
            method:'GET',
            headers:{
                "Content-Type":"application/json",
                "auth-Token":token
            }
        });
        const data = await response.json()

        return data

    }catch(error){
        throw error
    }
}


const Get_TeamPlayer_By_Id_API = async (teamId)=>{
    try{
        const response = await fetch(`${host}/getTeam/APIGetPlayerTeamId/${teamId}/${User_Code}`,{mode:'cors'},{
            method:'GET',
            headers:{"Content-Type":"application/json"}
        });

        const data = await response.json()

        return data

    }catch(error){
        throw error
    }
}


const Get_TeamPlayer_By_PlayerId_API = async (playerId)=>{
    try{
        const response = await fetch(`${host}/getTeam/APIGetPlayerInfoPlayerInfo//${playerId}/${User_Code}`,{mode:'cors'},{
            method:'GET',
            headers:{"Content-Type":"application/json"}
        });

        const data = await response.json()

        return data

    }catch(error){
        throw error
    }
}




export { Get_Team_Data_API, Get_TeamPlayer_By_Id_API, Get_TeamPlayer_By_PlayerId_API }