import React from 'react';
import '../style/main.css'


const Pedido = () => {
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
                        <h3>Bodega "Las palmeras"</h3>
                    </div>
                    <div className='mb-2'>
                        <form action = "">
                            <select class="form-select" aria-label="Default select example">
                                <option selected>Productos disponibles</option>
                                <option value="1">Leche</option>
                                <option value="2">Galletas</option>
                                <option value="3">Arroz</option>
                                <option value="4">Chocolate</option>
                            </select>
                            <div className='mt-4'>
                                <label>Cantidad: </label>
                                <input type="number"  min="0" pattern="^[0-9]+" className="form-control" placeholder="Ingresa la cantidad"></input>
                            </div>
                            <div className='mb-2 mt-3 text-center'>
                                <button className='btn btn-warning w-50 fw-bold'>Realizar pedido</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
                
        </div>

          );
        }
        

        export default Pedido;