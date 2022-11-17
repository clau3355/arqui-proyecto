import React from 'react';

const registro = () => {
    return (
      <div className="container mt-3">
        <h1>Inicio</h1>
        <h1>Registro</h1>
          <div className="mb-3 row">
            <label for="staticEmail" className="col-sm-2 col-form-label">Nombre</label>
            <label for="staticEmail" className="col-sm-2 col-form-label">Apellido</label>
            <div className="col-sm-10">
                <input type='text' name='search' className='form-control'></input>
            </div>
        </div>
        <div className="mb-3 row">
            <label for="inputPassword" className="col-sm-2 col-form-label">Contraseña</label>
            <div className="col-sm-10">
            <input type='password' name='search' className='form-control'></input>
            </div>
        </div>

        <div className='mt-3'>
            <button className='btn btn-danger'>Olvide mi contraseña</button>
        </div>
        <div  className='mt-3'>
            <button className='btn btn-primary'>Registrarse</button>
        </div>
        

      </div>
    );
  }
  
  export default registro;