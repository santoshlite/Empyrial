import './App.css';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './pages';


function App() {
  return (
    <Router>
      <Switch>
        {/* The line below needs to be changed depending on gh-pages or 
        actual domain */}
        <Route path='/Empyrial' component={Home} exact />
      </Switch>
    </Router>
  );
}

export default App;
