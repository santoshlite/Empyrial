import './App.css';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './pages';
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyA6eJZFFNuhiQn5iueAJU1-_t3Ntg9WhC8",
  authDomain: "empyrial-2a9c7.firebaseapp.com",
  projectId: "empyrial-2a9c7",
  storageBucket: "empyrial-2a9c7.appspot.com",
  messagingSenderId: "578952659778",
  appId: "1:578952659778:web:6f21fea33819d3bd353edb",
  measurementId: "G-EGSZVHRZH7"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);


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
