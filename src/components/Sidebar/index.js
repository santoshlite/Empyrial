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
          <SidebarLink to='engine' onClick={toggle}>
            Engine
          </SidebarLink>
          <SidebarLink to='fundamental' onClick={toggle}>
            Fundlens
          </SidebarLink>
          <SidebarLink to='services' onClick={toggle}>
            About
          </SidebarLink>
          <SidebarLink to='optimizer' onClick={toggle}>
            Optimizer
          </SidebarLink>
          <SidebarLink to='oracle' onClick={toggle}>
            Oracle
          </SidebarLink>
          <SidebarLink to='risk' onClick={toggle}>
            Riskslens
          </SidebarLink>
          <SidebarLink to='sentiment' onClick={toggle}>
            Sentiment
          </SidebarLink>
        </SidebarMenu>
        <SideBtnWrap>
          <SidebarRoute to='/contact'>Github</SidebarRoute>
        </SideBtnWrap>
      </SidebarWrapper>
    </SidebarContainer>
  );
};

export default Sidebar
