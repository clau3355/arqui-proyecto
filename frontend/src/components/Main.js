import React from 'react';
import usuario from '../images/usuario.png';

const Main = () => {
    return (
      <div className="d-flex mt-3 justify-content-center p-5">
        <div className='card col-sm-6 p-5' >
          <div className="mb-3">
            <h3>Menu principal</h3>
            <div className='text-center mt-4'>
            <div className='text-center'>
                                    <img src={usuario} size= "small" width = "200 px" heigth= "200 px"  alt='usuario.png' className='w-5'></img>
                                </div>

                <a className='btn btn-warning w-50 fw-bold' href='/login'>Iniciar Sesion</a>
            </div>
          </div>
          <hr></hr>
          <div className='text-center mt-4'>
            <a className='btn btn-primary w-50 fw-bold' href='/registro'>Registrarse</a>
          </div>
        </div>
      </div>
    );
  }
  
  export default Main;



