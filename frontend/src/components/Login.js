import React from 'react';
import '../style/index.css'

const Login = () => {
    return (
      <div className="d-flex mt-3 justify-content-center p-5">
        <div className='card col-sm-6 p-5' >
          <div className="mb-3">
            <h3>Iniciar Sesion</h3>
          </div>
          <div className='mb-2'>
            <form action = "">
              <div className='mb-2'>
                <label className="form-label">Correo</label>
                <input type="email" className="form-control" id="exampleFormControlInput1" placeholder="Ingresa tu correo"></input>
              </div>
              <div className='mb-2'>
                <label className="form-label">Contraseña</label>
                <input type="password" className="form-control" id="exampleFormControlInput1" placeholder="Ingresa tu contraseña"></input>
              </div>
              <div className='mb-2 mt-3 text-center'>
                <button className='btn btn-warning w-50 fw-bold'>Iniciar sesion</button>
              </div>
              <div className='mb-2 mt-3 text-center'>
                <a href='/' className='link'>Olvide mi contraseña</a>
              </div>
            </form>
          </div>
          <hr></hr>
          <div className='text-center mt-4'>
            <button className='btn btn-primary w-50 fw-bold'>Registrarse</button>
          </div>
        </div>
      </div>
    );
  }
  
  export default Login;