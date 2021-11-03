import React, {useEffect, useState} from 'react';
import { 
  Nav, 
  NavbarContainer, 
  NavLogo, 
  MobileIcon, 
  NavItem, 
  NavMenu, 
  NavLinks, 
  NavBtn,
  NavBtnLink,
} from './NavbarElements';
import { FaBars } from 'react-icons/fa'
import { animateScroll as scroll } from 'react-scroll';

const Navbar = ({ toggle }) => {
  const [scrollNav, setScrollNav] = useState(false);

  const changeNav = () => {
    if(window.scrollY >= 80) {
      setScrollNav(true)
    } else {
      setScrollNav(false)
    }
  };

  useEffect(() => {
    window.addEventListener('scroll', changeNav)
  }, []);

  const toggleHome = () => {
    scroll.scrollToTop();
  };

  return (
    <>
      <Nav scrollNav={scrollNav}>
        <NavbarContainer>
          <NavLogo to='/' onClick={toggleHome}>EMPYRIAL</NavLogo>
          <MobileIcon onClick={toggle}>
            <FaBars />
          </MobileIcon>
          <NavMenu>
            <NavItem>
              <NavLinks to='engine'
              smooth={true}
              duration={500}
              spy={true}
              exact='true'
              offset={-80}
              >Engine</NavLinks>
            </NavItem>
            <NavItem>
               <NavLinks to='fundamental'
               smooth={true}
               duration={500}
               spy={true}
               exact='true'
               offset={-80}
               >Fundlens</NavLinks>
            </NavItem>
            <NavItem>
               <NavLinks to='services'
               smooth={true}
               duration={500}
               spy={true}
               exact='true'
               offset={-80}
               >About</NavLinks>
            </NavItem>
            <NavItem>
              <NavLinks to='oracle'
              smooth={true}
              duration={500}
              spy={true}
              exact='true'
              offset={-80}
              >Oracle</NavLinks>
            </NavItem>
            <NavItem>
              <NavLinks to='optimizer'
              smooth={true}
              duration={500}
              spy={true}
              exact='true'
              offset={-80}
              >Optimizer</NavLinks>
            </NavItem>
            <NavItem>
              <NavLinks to='risk'
              smooth={true}
              duration={500}
              spy={true}
              exact='true'
              offset={-80}
              >Risklens</NavLinks>
            </NavItem>
            <NavItem>
              <NavLinks to='sentiment'
              smooth={true}
              duration={500}
              spy={true}
              exact='true'
              offset={-80}
              >Sentiment Lens</NavLinks>
            </NavItem>
            </NavMenu>
            <NavBtn>
              <NavBtnLink href='https://github.com/ssantoshp/Empyrial'>Github</NavBtnLink>
            </NavBtn>
        </NavbarContainer>
      </Nav>
    </>
  );
};

export default Navbar
