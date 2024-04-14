import React, { useEffect, useContext } from 'react'
import ModuleFirstPage from '../../others/ModuleFirstPage'
import noteContext from '../../../contexts/notes/NoteContext'
import { useParams, useNavigate } from 'react-router-dom'

const Recent_Match_Score_HTML = ({ setProgress, showAlert }) => {

  let history = useNavigate();
  const { matchId } = useParams();

  const contexts = useContext(noteContext)

  const { notes, GetMatchScore } = contexts

  useEffect(() => {
    setProgress(40)
    setTimeout(() => {
      GetMatchScore(matchId);

      setProgress(100)
    }, 1000)

    // eslint-disable-next-line
  }, [])


  const handledAPICall = () => {
    showAlert('Clicked', 'success')
  }


  return (
    <div className="main-section-container">
      {notes.map((item, index) => (
        <React.Fragment key={index}>
          {index === 0 && <ModuleFirstPage Title={item.Series_Description} Onclick={handledAPICall}></ModuleFirstPage>}
        </React.Fragment>
      ))}


      <div className="right-content">
        <div className="tabs-container-matchList">
          <div className="tabs-header-matchList" id="tab-header">

          </div>
          <div className="packs-card-container-matchList" id="packs-card-container">
            {notes.length === 0 && 'No score to display'}
            {notes.map((item, index) => (
              <div className="pack-card-content-matchList" key={index}>
                <div className="pack-card-left-section-matchList">
                  <div className="pack-card-details-matchList">
                    <div className="pack-card-detail-matchList">
                      <h4 className="pack-card-heading-matchList"> {item.Series_Description}  </h4>
                    </div>

                    <div className="pack-card-detail-matchList">
                      <h4 className="pack-card-heading-matchList"> {item.Team_Name}  </h4>
                    </div>

                    <div className="pack-card-detail-matchList image-attachment">
                      <img className="pack-card-heading-img" src={item.Image_URL} alt='None' />
                    </div>

                  </div>
                </div>
                <div className="pack-card-right-section">
                  <button className="btn btn-outline-danger mx-2" id={`button-${item.Player_Id}`} onClick={() => history({
                    pathname: `/get_recentMatch/get_score/score_details/${item.Match_Id}/${item.Team_Id}/${item.Bowl_Team_Id}`,
                    state: { matchId: item.Match_Id, teamId: item.Team_Id, bowlTeamId: item.Bowl_Team_Id }
                  })}>Get</button>
                </div>
              </div>


            ))}
          </div>
        </div>

      </div>
    </div>
  )
}

export default Recent_Match_Score_HTML
