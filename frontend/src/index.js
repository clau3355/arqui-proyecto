import React from 'react';
import ReactDOM from 'react-dom/client';
import './style/index.css';
//import Login from './components/Login';
//import Registro from './components/Registro';

//import Inicio from './components/Inicio';
import Tiendas from './components/Tiendas';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Tiendas />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
