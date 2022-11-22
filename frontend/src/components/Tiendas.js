import React from 'react';
import '../style/tienda.css'
import Ph from '../images/Ph.jpg';
import tienda from '../images/tienda.jpg';

const Tiendas = () => {
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
                                <a className="nav-link active" aria-current="page" href="/inicio">Inicio</a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link active" aria-current="page" href="/pedido">Pedido</a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link active" aria-current="page" href="/tiendas">Tiendas</a>
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
                <div className='col'>
                    <div className='row'>
                        <div className='card'>
                            <div className="card-body">
                                <h5 className="card-title">Bodega "Las palmeras"</h5>
                                <div className='text-center'>
                                    <img src={tienda} size= "small" alt='tienda.png' className='w-10'></img>
                                </div>
                                <p className="card-text">
                                 
                                <h3>Unicación : Av. los tulipanes A-18</h3>
                                  
                                    
                                </p>
                                <div className='text-center'>


                                    <a href="/pedido" className="btn btn-primary">Elegir Tienda</a>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                    
                </div>         
                </div>
                </div>

                <div className='container p-4'>
                <div className='col'>
                    <div className='row'>
                        <div className='card'>
                            <div className="card-body">
                                <h5 className="card-title">Pizza Hut</h5>
                                <div className='text-center'>
                                    <img src={Ph} alt='Ph.png' className='w-10'></img>
                                </div>
                                <p className="card-text">
                                  
                                <h3>Ubicación : Av. los tulipanes A-18</h3>
                                 
                                    
                                </p>
                                <div className='text-center'>


                                    <a href="/" className="btn btn-primary">Elegir Restaurante</a>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                    
                </div>         
                </div>
                
                
            
        

        

                












        </div>
        


          );
        }
        

        export default Tiendas;