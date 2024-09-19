import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Link } from "react-router-dom";






function Home() {
  return (
    <div className="App">
      <h1>Welcome To Hame Page</h1>
      <h2>Wish You good luck</h2>
    </div>
  );
}


function Profile() {
  return (
    <div className="App">
      <h1>Welcome To Profile Page</h1>
      <h2>Pleased to meet you</h2>
    </div>
  );
}

function NavBar() {
  return (
    <div className="App">
      <h1>NavBar</h1>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/profile">Profile</Link>
        </li>
      </ul>
    </div>
  );
}



function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <NavBar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/profile" element={<Profile />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
