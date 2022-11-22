import {BrowserRouter as Router,Routes,Route} from 'react-router-dom';
import Inicio from './components/Inicio';
import Login from './components/Login';
import Registro from './components/Registro';
import Tiendas from './components/Tiendas';
import Pedido from './components/Pedido';

function App() {
  return (
    <div>
      <Router>
        <Routes>
          <Route path='/' element ={<Inicio />}/>
          <Route path='/login' element ={<Login />}/>
          <Route path='/registro' element ={<Registro />}/>
          <Route path='/tiendas' element ={<Tiendas />}/>
          <Route path='/pedido' element ={<Pedido />}/>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
  