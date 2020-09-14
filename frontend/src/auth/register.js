import React, { useState } from 'react';
import { useHistory } from 'react-router';
import { Form, Button, Alert } from 'react-bootstrap';
import auth from './auth';

export const Register = () => {
  // History hook
  const history = useHistory();

  // User information hook
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [passwordConfirmation, setPasswordConfirmation] = useState('');
  const [error, setError] = useState('');

  // Function to call submit
  const callSubmit = async (e) => {
    // Prevents page reload on wrongs creds
    e.preventDefault();
    setError('');
    try {
      const data = await auth.register(firstName, lastName, email, password, passwordConfirmation);
      // Executes only when there are no 400 and 500 errors, else they are thrown as errors
      // Callbacks can be added here
      if (data) {
        await auth.login(email, password);
        alert('Registration Successful!');
        history.push('/');
      }
    }
    catch (err) {
      if (err instanceof Error) {
        // Handle errors thrown from frontend
        setError(err.message);
      } 
      else {
        // Handle errors thrown from backend
        if (err === 'REGISTER_USER_ALREADY_EXISTS') {
          setError('Email ID is already registered. Please use your credentials to login.');
        }
        else {
          setError('Error occured in the API.');
        }
      }
    }
  };

  return (
    <>
      <h2>Register</h2>
      <Form onSubmit={callSubmit}>
        <Form.Group controlId="formRegisterFirstname">
          <Form.Label>First Name</Form.Label>
          <Form.Control type="text" placeholder="Enter first name" value={firstName} onChange={(f) => setFirstName(f.currentTarget.value)} />
        </Form.Group>
        <Form.Group controlId="formRegisterLastname">
          <Form.Label>Last Name</Form.Label>
          <Form.Control type="text" placeholder="Enter last name" value={lastName} onChange={(l) => setLastName(l.currentTarget.value)} />
        </Form.Group>
        <Form.Group controlId="formRegisterEmail">
          <Form.Label>Email</Form.Label>
          <Form.Control type="email" placeholder="Enter email" value={email} onChange={(e) => setEmail(e.currentTarget.value)} />
        </Form.Group>
        <Form.Group controlId="formRegisterPassword">
          <Form.Label>Password</Form.Label>
          <Form.Control type="password" placeholder="Enter password" value={password} onChange={(p) => setPassword(p.currentTarget.value)}/>
        </Form.Group>
        <Form.Group controlId="formRegisterPasswordConfirmation">
          <Form.Label>Confirm Password</Form.Label>
          <Form.Control type="password" placeholder="Confirm password" value={passwordConfirmation} onChange={(p) => setPasswordConfirmation(p.currentTarget.value)}/>
        </Form.Group>
        <Alert variant='danger' style={ error!=='' ? {display:"block"} : {display:"none"}}>
          {error}
        </Alert>
        <Button variant="primary" type="submit" block>
          Register
        </Button>
      </Form>
    </>
  );
};
