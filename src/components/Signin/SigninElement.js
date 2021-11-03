import styled from 'styled-components';
import { Link } from 'react-router-dom';


export const Container = styled.div`
  min-height: 692px;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  top: 0;
  z-index: 0;
  overflow: hidden;
  background: linear-gradient(
  108deg,
  rgba(1, 147, 86, 1) 0%,
  rgba(10, 201, 122, 1) 100%
  ); 
`;

export const FormWrap = styled.div`
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  
  @media screen and (max-width: 400px) {
    height: 80%;
  }
`;

export const Icon = styled(Link)`
  margin-left: 32px;
  margin-top: 32px;
  text-decoration: nopne;
  color: #fff;
  font-weight: 700px;
  font-size: 32px;

  @media screen and (max-width: 480px) {
    margin-left: 16px;
    margin-top: 25px;
  } 
`;

export const FormContent = styled.div`
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;

  @media screen and (max-width: 480px) {
    padding: 10px;
  }
`;

export const Form = styled.form`
  background: #010101;
  max-width: 600px;
  height: auto;
  width: 100%;
  z-index: 1;
  display: grid;
  margin: 0 auto;
  padding: 80px 32px;
  border-radius: 4px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.9);

  @media screen and (max-width: 400px) {
    padding: 32px 32px;
    max-width: 230px;
    max-height: 585px;
  }

  @media screen and (max-height: 600px) {
    max-height: 430px;
    padding: 20px 20px;
    width: auto;
  }
`;

export const FormH1 = styled.h1`
  margin-bottom: 40px;
  font-size: 20px;
  color: #fff;
  font-weight: 400;
  text-align: center;
`

export const FormLabel = styled.label`
  margin-bottom: 8px;
  font-size: 14px;
  color: #fff;

  @media screen and (max-height: 600px) {
    margin-bottom: 15px;
    font-size: 10px;
  }
`;

export const FormInput = styled.input`
  padding: 16px 16px;
  margin-bottom: 32px;
  border: none;
  border-radius: 4px;

  @media screen and (max-width: 400px) {
    max-width: 160px;
    height: 22px;
  }

  @media screen and (max-width: 200px) {
    max-width: auto;
    height: auto;
  }

  @media screen and (max-height: 600px) {
    height: 10px;
  }
`;

export const FormInputMessage = styled.textarea`
  padding: 16px 16px;
  margin-bottom: 32px;
  border: none;
  border-radius: 4px;
  height: 100px;
  width: auto;
  text-align: top;

  @media screen and (max-width: 400px) {
    max-width: 160px;
    height: 22px;
  }

  @media screen and (max-height: 600px) {
    height: 10px;
  }
`;

export const FormButton = styled.button`
  background: #01bf71;
  padding: 16px 0;
  border: none;
  border-radius: 4px;
  color: #fff;
  font-size: 20px;
  cursor: pointer;
  width: 160px;

  @media screen and (max-width: 400px) {
    width: 100%;
    height: auto;
    font-size: 14px;
    justify-content: center;
  }

  @media screen and (max-height: 600px) {
    height: 10px;
    font-size: 10px;
    width: 80%;
  }
`;

export const LinkE = styled.a`
  text-decoration: none;
  color: #fff;
`;
