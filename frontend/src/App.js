import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Home } from './pages/Home';
import { ProtectedRoute } from './auth/protected-route';
import './App.css';

function App() {
  return (
    // Router Code
    <BrowserRouter>
      <div  className="App">
        <ProtectedRoute 
            path='/'
            exact 
            strict
            component = {Home}
          />
        {/* <Route 
            path='/anotherpage'
            exact 
            strict
            component = {AnotherPage}
          /> */}
       </div>
    </BrowserRouter>
  );
};
export default App;
