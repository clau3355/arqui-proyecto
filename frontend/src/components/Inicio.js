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
                                <h5 className="card-title">Perfil</h5>
                                <div className='text-center'>
                                    <img src={user} alt='user.png' className='w-50'></img>
                                </div>
                                <p className="card-text">
                                <h3>Datos : Lucas</h3>  
                                <h3>Direccion : Av. los tulipanes A-18</h3>
                                <h3>telefono : 984999965</h3>  
                                    
                                </p>
                                <div className='text-center'>


                                    <a href="/" className="btn btn-primary">Ver más información</a>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                    <div className='col'>
                        <div className='card'>
                                <div className="card-body">
                                    <h5 className="card-title">Pedido</h5>
                                    <p className="card-text">Vizualizar el estado de tu pedido:</p>
    
                                    <div  className='mt-3'>
                                    <button className='btn btn-primary'>Estado</button>
                                    <h1></h1>
                                    <div className="col-sm-10">
                                    <input type='text' name='search' className='form-control'></input>
                                    </div>
                                    </div>
                                    <div  className='mt-3'>
                                    <button className='btn btn-primary'>Mapa</button>
                                    

                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className='col'>
                        <div className='card'>
                                <div className="card-body">
                                    <h5 className="card-title">Contacto</h5>
                                    <p className="card-text">Contactar al repartidor :</p>

                                    <div  className='mt-3'>
                                    <button className='btn btn-primary'>Chat</button>
                                    <div  className='mt-3'>
                                    <button className='btn btn-primary'>Videollamada</button>
                                    </div>

                                    </div>
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