
let host = process.env.REACT_APP_HOST;
let token = localStorage ? localStorage.getItem('auth-Token'):null;
let User_Code = localStorage ? localStorage.getItem('User_Code'):null

const Get_Match_List_API = async () =>{
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


export {Get_Match_List_API}