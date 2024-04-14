import React, { useEffect, useContext } from 'react'
import { useParams } from 'react-router-dom'
import noteContext from '../../../contexts/notes/NoteContext';
import ModuleFirstPage from '../../others/ModuleFirstPage';

const GetPlayerDetHTML = ({ setProgress,showAlert }) => {

  const { teamId } = useParams();
  const { playerId } = useParams();
  const context = useContext(noteContext)

  const { notes, GetPlayerDetailsList, teamName, GetPlayerNameId,GetPlayerInfoByPlayerIdAPI } = context


  //Fetch the player info while click on the particular player from previous page (GET)
  useEffect(() => {
    setProgress(40)

    setTimeout(() => {
      setProgress(100)
      GetPlayerDetailsList(playerId,teamId)
      GetPlayerNameId(playerId,teamId)
    }, 1000)
    // eslint-disable-next-line
  }, [])


// Function to call the API of particular player info (API)
const handleClickPlayerInfoAPI = async (playerId) =>{
  try{
    setProgress(40)
    const response = await GetPlayerInfoByPlayerIdAPI(playerId)
    let Error_Code = response.message[0].Error_Code
    let Error_Name = response.message[0].Error_Name

    setTimeout(()=>{
      let alertMessage = ""

      if (Error_Code === 0) {
        alertMessage = "success"
        GetPlayerDetailsList(playerId,teamId)
      }
      else {
        alertMessage = "danger"
      }

      showAlert(Error_Name, alertMessage)
      setProgress(100)
    },1000)


  } catch(error){

  }
}

  return (
    <div className='main-section-container'>
      {teamName.map((item,index)=>(
        <ModuleFirstPage Title={item.Player_Name} key={index} Onclick={()=>{handleClickPlayerInfoAPI(playerId)}}></ModuleFirstPage>
      ))}
      
        <div className="right-content" >
          <div className="packs-card-container" id="packs-card-container">
          {notes.length === 0 && 'No player info to display'}
          {notes.map((item) => (
            <div className="container" key={item.Player_Id}>
              <div className="row">
                <div className="col my-5">
                  <h3> {item.Player_Name} </h3>
                  <h3> {item.Role} </h3>
                  <h3> {item.DOB} </h3>
                  <h3> {item.Intl_Team} </h3>
                </div>
                <div className="col  my-5">
                  <img className='img-thumbnail rounded float-left' src={item.Image_URL} alt='None'></img>
                </div>
                <div className="col my-5">
                  <h3> {item.Batting_Style} </h3>
                  <h3> {item.Bowling_Style} </h3>
                </div>
              </div>
              <div style={{ height: 'calc(100vh - 450px)', overflow: "auto" }}>
                <p className='h4'>{item.Bio}</p>
              </div >
            </div>
          ))}
          </div>
        </div>
    </div>
  )
}

export default GetPlayerDetHTML
