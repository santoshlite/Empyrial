import React from 'react';
import Axios from 'axios';
import {
  Container,
  FormWrap,
  Icon,
  FormContent,
  Form,
  FormH1,
  FormLabel,
  FormInput,
  FormButton,
  FormInputMessage,
  LinkE
} from './SigninElement';
import ParticlesBg from 'particles-bg';

class Signin extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            name: '',
            email: 'brendan@cantonchamber.org',
            message: '',
            disabled: false,
            emailSent: null,
        }
    }


    handleChange = (event) => {
        const target = event.target;
        const value = target.type === 'checkbox' ? target.checked : target.value;
        const name = target.name;

        this.setState({
            [name]: value
        })
    }


    handleSubmit = (event) => {
        event.preventDefault();

        console.log(event.target);

        this.setState({
            disabled: true
        });

        Axios.post('http://localhost:3030/api/email', this.state)
            .then(res => {
                if(res.data.success) {
                    this.setState({
                        disabled: false,
                        emailSent: true
                    });
                } else {
                    this.setState({
                        disabled: false,
                        emailSent: false
                    });
                }
            })
            .catch(err => {
                console.log(err);

                this.setState({
                    disabled: false,
                    emailSent: false
                });
            })

    }


    render() {
        return(
           <>
      <Container>
        <FormWrap>
          <Icon to="/">DKL</Icon>
          <ParticlesBg type="circle" bg={true} />
          <FormContent>
            <Form onSubmit={this.handleSubmit}>
              <FormH1>Contact us for a speedy quote</FormH1>
              <FormLabel htmlFor='full-name'>Full Name</FormLabel>
                <FormInput 
              id="full-name" 
              name="name" 
              type="text" 
              value={this.state.name} 
              onChange={this.handleChange} />
                <FormLabel htmlFor='message'>
                Message</FormLabel>
                <FormInputMessage 
                  id="message" 
                  name="message" 
                  as="textarea"rows="3" 
                  value={this.state.message} 
              onChange={this.handleChange} />
              <FormButton 
                type='submit' 
                className="d-inline-block" 
                variant="primary" 
                type="submit" 
                disabled={this.state.disabled}>
                <LinkE>
              Send message</LinkE></FormButton>
               {this.state.emailSent === true && <p className="d-inline success-msg">Email Sent</p>}
                        {this.state.emailSent === false && <p className="d-inline err-msg">Email Not Sent</p>}
            </Form>
          </FormContent>
        </FormWrap>
      </Container>
    </>
        );
    }

}

export default Signin;
