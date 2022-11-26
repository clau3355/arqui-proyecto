import React from 'react';
import {BrowserRouter as Router,Routes,Route} from 'react-router-dom';
import Inicio from './components/Inicio';
import Login from './components/Login';
import Registro from './components/Registro';
import Tiendas from './components/Tiendas';
import Pedido from './components/Pedido';
import Main from './components/Main';
import Mapa from './components/mapa';
import Final from './components/final';

function App() {
  return (
    <div>
      <Router>
        <Routes>
          <Route path='/' element ={<Main />}/>
          <Route path='/inicio' element ={<Inicio />}/>
          <Route path='/login' element ={<Login />}/>
          <Route path='/registro' element ={<Registro />}/>
          <Route path='/tiendas' element ={<Tiendas />}/>
          <Route path='/pedido' element ={<Pedido />}/>
          <Route path='/mapa' element ={<Mapa />}/>
          <Route path='/final' element ={<Final />}/>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
  