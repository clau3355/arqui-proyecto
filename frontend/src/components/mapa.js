import React from 'react';
import '../style/main.css'


const Mapa = () => {
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

        <div className="d-flex mt-3 justify-content-center p-5">
        <div className='card col-sm-6 p-5' >
          <div className="mb-3">
            <h3>Calculo de ruta</h3>

            <div class ="container-fluid">
                    <div id="map">

                    </div>

                    <div id="output">

                    </div>
               </div>
               
          </div>
          <div className='mb-2'>
            <form action = "">
            <a className='btn btn-primary' href='/final'>Continuar</a>  
            </form>
          </div>
        
        </div>
      </div>
        </div>

          );
        }
        

export default Mapa;