import React from 'react';


const Main = () => {
    return (
      <div className="d-flex mt-3 justify-content-center p-5">
        <div className='card col-sm-6 p-5' >
          <div className="mb-3">
            <h3>Menu principal</h3>
            <div className='text-center mt-4'>
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



