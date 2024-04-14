
import React, { useContext, useEffect } from 'react'
import noteContext from '../../../contexts/notes/NoteContext'
import ModuleFirstPage from '../../others/ModuleFirstPage';
import { useNavigate } from 'react-router-dom';


const Get_Team = ({ setProgress, showAlert }) => {

  const contexts = useContext(noteContext)
  const { notes, GetTeamList, GetTeamListAPI } = contexts
  let history = useNavigate();


  // This is use for to get all the team list while page loading (GET)

  useEffect(() => {
    setProgress(40)

    setTimeout(() => {
      setProgress(100)
      GetTeamList('International')
      cssClass('International')
    }, 1000)
    // eslint-disable-next-line
  }, [])


  //  Function to handle the get all the team list on the page load using API (API)

  const handledAPICall = async () => {
    try {
      setProgress(40)

      const response = await GetTeamListAPI()
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
        GetTeamList()
      }, 1000)

    } catch (error) {
      throw error
    }
  }

  const handledTeamType = (teamType) =>{
    cssClass(teamType)
    GetTeamList(teamType)
  }

  const cssClass = (teamType)=>{
    try{
      const tabs = document.querySelectorAll('.tabs-header-content-text');
      tabs.forEach(tab => {
        tab.classList.remove('active');
      });
      const clickedTab = document.getElementById(`tab-header-span-${teamType}`);
      clickedTab.classList.add('active');
    }catch(error){
      throw error
    }
  }

  return (
    <div className="main-section-container">
      <ModuleFirstPage Title="Team List" Onclick={handledAPICall}></ModuleFirstPage>
      <div className="right-content">
        <div className="tabs-container">
          <div className="tabs-header" id="tab-header">
              <div className={`tabs-header-content`} ><span className="tabs-header-content-text" id="tab-header-span-Domestic" onClick={()=>{handledTeamType('Domestic')}}>Domestic</span></div>
              <div className={`tabs-header-content`} ><span className="tabs-header-content-text" id="tab-header-span-International" onClick={()=>{handledTeamType('International')}}>International</span></div>
              <div className={`tabs-header-content`} ><span className="tabs-header-content-text" id="tab-header-span-League" onClick={()=>{handledTeamType('League')}}>League</span></div>
              <div className={`tabs-header-content`} ><span className="tabs-header-content-text" id="tab-header-span-women" onClick={()=>{handledTeamType('women')}}>Women</span></div>
          </div>
          <div className="packs-card-container" id="packs-card-container">
            {notes.length === 0 && 'No teams to display'}
            {notes.map((item, index) => (
              <div className="pack-card-content" key={index}>
                <div className="pack-card-left-section">
                  <div className="pack-card-details">
                    <div className="pack-card-detail">
                      <h4 className="pack-card-heading"> {item.Team_Code}  </h4>
                    </div>
                    <div className="pack-card-detail">
                      <h4 className="pack-card-heading">  {item.Team_Name}  </h4>
                    </div>
                    <div className="pack-card-detail image-attachment">
                      <img className="pack-card-heading-img" src={item.Images} alt="" />
                    </div>
                  </div>
                </div>
                <div className="pack-card-right-section">
                  <button className="btn btn-outline-danger mx-2" id={`button-${item.Team_Id}`} onClick={() => history({pathname:`/get_teamList/player_details/${item.Team_Id}`,
                                                                                                                        state:{teamId:item.Team_Id}})}>Get</button>
                </div>
                
              </div>
            ))}
          </div>
        </div>
      </div>

    </div>
  )
}

export default Get_Team
