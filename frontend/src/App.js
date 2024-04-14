import React, { useState } from 'react'
import {
  BrowserRouter as Router,
  Routes,
  Route
} from "react-router-dom";
import Navbar from './component/others/Navbar';
import NoteState from './contexts/notes/NoteState'
import Home from './component/others/Home'
import GetTeamHTML from './component/modules/TeamList/Get_Team_HTML';
import LoadingBar from 'react-top-loading-bar'
import './App.css';
import '../src/css/matchList/MatchList.css'
import GetTeamPlayer from './component/modules/TeamList/Get_Team_Player_HTML';
import GetPlayerDetHTML from './component/modules/TeamList/Get_Player_Det_HTML';
import RecentMatchListHTML from './component/modules/MatchList/Recent_Match_List_HTML'
import RecentMatchScoreHTML from './component/modules/MatchList/Recent_Match_Score_HTML'
import RecentMatchScoreDetailsHTML from './component/modules/MatchList/Recent_Match_Score_Details'
import Alert from './component/others/Alert';
import Login from './component/others/Login';
function App() {

  const [progress, setProgress] = useState(0)

  const [alert, setAlert] = useState('')
  
  const showAlert = (message,type)=>{
    setAlert({msg:message,types:type})
  }

  setTimeout(()=>{
    setAlert(null)
  },3000)

  return (
    <>
      <NoteState>
        <Router>
          <Navbar></Navbar>
          <Alert alert={alert}></Alert>
          <LoadingBar
            color='#f11946'
            progress={progress}
            onLoaderFinished={() => setProgress(0)}
          />
          <Routes>
            <Route exact path="/" element={<Home setProgress={setProgress}></Home>} ></Route>
            <Route exact path="/get_teamList" element={<GetTeamHTML setProgress={setProgress} showAlert={showAlert}></GetTeamHTML>} ></Route>
            <Route exact path="/get_teamList/player_details/:teamId" element={<GetTeamPlayer setProgress={setProgress} showAlert={showAlert}></GetTeamPlayer>} ></Route>
            <Route exact path="/get_teamList/player_details/player_info/:playerId/:teamId" element={<GetPlayerDetHTML setProgress={setProgress} showAlert={showAlert}></GetPlayerDetHTML>} ></Route>
            <Route exact path="/login" element={<Login setProgress={setProgress}></Login>} ></Route>
            <Route exact path="/get_recentMatch" element={<RecentMatchListHTML setProgress={setProgress} showAlert={showAlert}></RecentMatchListHTML>}></Route>
            <Route exact path="/get_recentMatch/get_score/:matchId" element={<RecentMatchScoreHTML setProgress={setProgress} showAlert={showAlert}></RecentMatchScoreHTML>}></Route>
            <Route exact path="/get_recentMatch/get_score/score_details/:matchId/:teamId/:bowlTeamId" element={<RecentMatchScoreDetailsHTML setProgress={setProgress} showAlert={showAlert}></RecentMatchScoreDetailsHTML>}></Route>
          </Routes>
        </Router>
      </NoteState>
    </>
  );
}

export default App;
