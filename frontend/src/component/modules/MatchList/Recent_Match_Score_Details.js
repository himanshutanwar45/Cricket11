import React, { useContext, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import noteContext from '../../../contexts/notes/NoteContext'
import ModuleFirstPage from '../../others/ModuleFirstPage'

const Recent_Match_Score_Details = ({ setProgress, showAlert }) => {

    const { matchId, teamId, bowlTeamId } = useParams();

    const context = useContext(noteContext)

    const { notes, GetMatchScoreBatter, GetMatchScoreBowler } = context

    useEffect(() => {
        setProgress(40);
        setTimeout(() => {
            GetMatchScoreBatter(matchId, teamId)
            setProgress(100)
        }, 1000)

        setTimeout(() => {
            cssClass('Batter')
        }, 1500)

        // eslint-disable-next-line
    }, [])


    const handledAPICall = () => {
        showAlert('Clicked', 'success')
    }

    const handledClickonTab = async (Item) => {
        try {
            cssClass(Item)
            if (Item === 'Batter') {
                setProgress(40);
                setTimeout(()=>{
                    GetMatchScoreBatter(matchId, teamId)
                    setProgress(100);
                },1000)
            } else if (Item === 'Bowler') {
                setTimeout(()=>{
                    GetMatchScoreBowler(matchId, bowlTeamId)
                    setProgress(100);
                },1000)
            }
        } catch (error) {
            throw error
        }

    }

    const cssClass = (Item) => {
        try {
            const tabs = document.querySelectorAll('.tabs-header-content-text-matchList');
            tabs.forEach(tab => {
                tab.classList.remove('active');
            });

            const clickedTab = document.getElementById(`tab-header-span-${Item}`);
            if (clickedTab) {
                clickedTab.classList.add('active');

            } else {
                throw new Error(`Element with ID 'tab-header-span-${Item}' not found`);
            }

        } catch (error) {
            throw error;
        }
    }

    return (
        <div className="main-section-container">
            <ModuleFirstPage Title="Score Details" Onclick={handledAPICall}></ModuleFirstPage>
            <div className="right-content">
                <div className="tabs-container-matchList">
                    <div className="tabs-header-matchList" id="tab-header">
                        <div className={`tabs-header-content-matchList`}><span className="tabs-header-content-text-matchList" style={{'cursor':'pointer'}} id={`tab-header-span-Batter`} onClick={() => { handledClickonTab('Batter') }}>Batter</span></div>
                        <div className={`tabs-header-content-matchList`}><span className="tabs-header-content-text-matchList" style={{'cursor':'pointer'}} id={`tab-header-span-Bowler`} onClick={() => { handledClickonTab('Bowler') }}>Bowler</span></div>
                    </div>
                    <div className="packs-card-container-matchList" id="packs-card-container">
                    {notes.length === 0 && 'No score to display'}
                        {notes.map((item, index) => (
                            <div className="pack-card-content-matchList" key={index}>
                                <div className="pack-card-left-section-matchList">
                                    <div className="pack-card-details-matchList">
                                        <div className="pack-card-detail-matchList">
                                            <h5 className="pack-card-heading-matchList" > {item.Player_Name}  </h5>
                                            <h5 className="pack-card-heading-matchList">  {item.Team_Name}  </h5>
                                        </div>
                                        <div className="d-flex flex-row justify-content-between">
                                            <div className="pack-card-detail-matchList">
                                                <h5 className="pack-card-heading-matchList" style={{'width':'100px'}}>Runs: <strong>{item.Runs}</strong> </h5>
                                                <h5 className="pack-card-heading-matchList" style={{'width':'100px'}}>Fours: <strong>{item.Fours}</strong> </h5>
                                                <h5 className="pack-card-heading-matchList" style={{'width':'100px'}}>Sixes: <strong>{item.Sixes}</strong> </h5>
                                            </div>
                                            <div className="pack-card-detail-matchList">
                                                <img className="pack-card-heading-img-matchList" src={item.Image_URL} alt='None' />
                                            </div>
                                        </div>
                                        
                                    </div>
                                    {/* <div className="pack-card-benefits-heading" style={{'width':'100px'}}> Fours: {item.Fours}</div> */}
                                    {/* <br></br>
                                    <div className="pack-card-benefits-heading" style={{'width':'100px'}}>Sixes: {item.Sixes} </div> */}
                                </div>
                                {/* <div className="pack-card-right-section">
                                    <button className="btn btn-outline-danger mx-2" id={`button-${item.Match_Id}`} onClick={() => history({pathname:`/get_recentMatch/get_score/${item.Match_Id}`,
                                                                                                                        state:{teamId:item.Match_Id}})} >GET</button>
                                </div> */}

                                {/* <div className="pack-card-right-section">
                                    <button className="btn btn-outline-danger mx-2" id={`API-${item.Team_Id}`} >+</button>
                                </div> */}
                            </div>
                        ))}
                    </div>
                </div>

            </div>
        </div>
    )
}

export default Recent_Match_Score_Details
