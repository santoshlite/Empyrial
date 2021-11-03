import React from 'react';
import { SidebarContainer, 
  Icon, 
  CloseIcon, 
  SidebarWrapper, 
  SidebarMenu, 
  SidebarLink,
  SideBtnWrap,
  SidebarRoute
} from './SidebarElements';

const Sidebar = ({ isOpen, toggle }) => {
  return (
    <SidebarContainer isOpen={isOpen} onClick={toggle}>
      <Icon onClick={toggle}>
        <CloseIcon />
      </Icon>
      <SidebarWrapper>
        <SidebarMenu>
          <SidebarLink to='about' onClick={toggle}>
            Engine
          </SidebarLink>
          <SidebarLink to='discover' onClick={toggle}>
            Fundlens
          </SidebarLink>
          <SidebarLink to='services' onClick={toggle}>
            About
          </SidebarLink>
          <SidebarLink to='signup' onClick={toggle}>
            Optimizer
          </SidebarLink>
          <SidebarLink to='signup' onClick={toggle}>
            Oracle
          </SidebarLink>
          <SidebarLink to='signup' onClick={toggle}>
            Riskslens
          </SidebarLink>
        </SidebarMenu>
          <SidebarLink to='signup' onClick={toggle}>
            Sentiment
          </SidebarLink>
        <SideBtnWrap>
          <SidebarRoute to='/contact'>Github</SidebarRoute>
        </SideBtnWrap>
      </SidebarWrapper>
    </SidebarContainer>
  );
};

export default Sidebar
