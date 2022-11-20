import React from 'react';
import '../style/main.css'
import user from '../images/user.jpg';

const Inicio = () => {
    return (
      <div>
        <div>
            <nav className="navbar navbar-expand-lg bg-light">
                <div className="container-fluid">
                    <a className="navbar-brand fw-bold" href="/">Fast Delivery</a>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                            <li className="nav-item">
                                <a className="nav-link active" aria-current="page" href="/">Inicio</a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link active" aria-current="page" href="/">Pedido</a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link active" aria-current="page" href="/">Tiendas</a>
                            </li>
                        </ul>
                        <form className="d-flex" role="search">
                            <input className="form-control me-2" type="search" placeholder="Buscar" aria-label="Search"></input>
                            <button className="btn btn-outline-success" type="submit">Buscar</button>
                        </form>
                    </div>
                </div>
            </nav>
        </div>
        <div  className="main">
            <div className='p-3'>
                <h1 className='welcome'>Bienvenido</h1>
            </div>
            
            <div className='container p-4'>
                <div className='row'>
                    <div className='col'>
                        <div className='card'>
                            <div className="card-body">
                                <h5 className="card-title">Username</h5>
                                <div className='text-center'>
                                    <img src={user} alt='user.png' className='w-50'></img>
                                </div>
                                <p className="card-text">With supporting text below as a natural lead-in to additional content.</p>
                                <div className='text-center'>
                                    <a href="/" className="btn btn-primary">Go somewhere</a>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                    <div className='col'>
                        <div className='card'>
                                <div className="card-body">
                                    <h5 className="card-title">Pedidos</h5>
                                    <p className="card-text">With supporting text below as a natural lead-in to additional content.</p>
                                </div>
                            </div>
                        </div>
                </div>
            </div>

            <div className='mt-4'>
                <div className='text-center container'>
                    <div className='p-5'>
                        <a href="/" className='btn btn-primary w-25'> Hacer pedido</a>
                    </div>
                    
                </div>
                
            </div>
        </div>
      </div>
    );
  }
  
  export default Inicio;