
import './App.css';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import Profile from './pages/Profile.js';
import Commentary from './pages/Commentary.js';
import Rewards from './pages/Rewards.js';
import Home from './pages/Home.js';
import CommentaryHome from './pages/CommentaryHome.js';

function App() {
  return (
  <>
    <Router>
        {/* <NavBar /> */}
        <Route
          render={({ location }) => (
            // <AnimatePresence exitBeforeEnter>
              <Switch>
                <Route path="/" exact component={Home} />
                <Route path="/profile" exact component={Profile} />
                <Route path="/commentary/play" exact component={Commentary} />
                <Route path="/commentary" exact component={CommentaryHome} />
                <Route path="/rewards" exact component={Rewards} />
              </Switch>
            // </AnimatePresence>
          )}
        />
      </Router>
  </>
  );
}

export default App;
