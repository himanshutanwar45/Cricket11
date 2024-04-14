import React, { useEffect,useContext } from 'react'
import ModuleFirstPage from '../../others/ModuleFirstPage'
import noteContext from '../../../contexts/notes/NoteContext'
import { useParams,useNavigate } from 'react-router-dom'

const Get_Team_Player = ({ setProgress,showAlert }) => {
  let history = useNavigate();
  const { teamId } = useParams();
  const contexts = useContext(noteContext)
  const { notes, GetTeamPlayerList, GetPlayerByTeamIdAPI,teamName,GetTeamNameId } = contexts

  // Fetch the player list while click on the previous page of team id button (GET)
  useEffect(() => {
    setProgress(40)
    setTimeout(() => {
      setProgress(100)
      GetTeamPlayerList(teamId)
      GetTeamNameId(teamId)
    }, 1000)
    // eslint-disable-next-line
  }, [])

  // Function to call the API for getting the player data of a particular team   (API)
  const handledAPIPlayerList = async (teamId) => {
    try {
      setProgress(40)

      const response = await GetPlayerByTeamIdAPI(teamId)
      let Error_Code = response.message[0].Error_Code
      let Error_Name = response.message[0].Error_Name

      setTimeout(() => {
        let alertMessage = ""

        if (Error_Code === 0) {
          alertMessage = "success"
        }
        else {
          alertMessage = "danger"
        }

        showAlert(Error_Name, alertMessage)
        setProgress(100)
        GetTeamPlayerList(teamId)
      }, 1000)
    }
    catch (error) {
      throw error
    }
  }

  return (
    <div className="main-section-container">
      
      {teamName.length === 0 && 'No teamname to display'}
      {teamName.map((item,index)=>(
        <ModuleFirstPage Title={item.Team_Name} key={index} Onclick={()=>{handledAPIPlayerList(teamId)}}></ModuleFirstPage>
      ))}
      <div className="right-content" >
        <div className="packs-card-container" id="packs-card-container">
          {notes.length === 0 && 'No players to display'}
          {notes.map((item,index) => (
            <div className="pack-card-content" key={index}>
              <div className="pack-card-left-section">
                <div className="pack-card-details">
                  <div className="pack-card-detail">
                    <h4 className="pack-card-heading"> {item.Player_Name}  </h4>
                  </div>
                  <div className="pack-card-detail image-attachment">
                    <img className="pack-card-heading-img" src={item.Image_URL} alt='None' />
                  </div>
                </div>
              </div>
              <div className="pack-card-right-section">
                <button className="btn btn-outline-danger mx-2" id={`button-${item.Player_Id}`} onClick={() => history(`/get_teamList/player_details/player_info/${item.Player_Id}/${item.Team_Id}`)}>Get</button>
              </div>
              
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default Get_Team_Player
