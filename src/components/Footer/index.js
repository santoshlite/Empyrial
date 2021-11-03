import React from 'react';
import {
FooterContainer,
FooterWrap,
FooterLinksContainer,
FooterLinksWrapper,
FooterLinkItems,
FooterLinkTitle,
FooterLink,
Link1
} from './FooterElements';

const Footer = () => {
  return (
    <FooterContainer>
      <FooterWrap>
        <FooterLinksContainer>
          <FooterLinksWrapper>
            <FooterLinkItems>
              <FooterLinkTitle>Learn More</FooterLinkTitle>
              <FooterLink>
              <Link1 
              href="https://github.com/ssantoshp/Empyrial" 
              target="_blank" 
              rel="noreferrer">
              Github</Link1></FooterLink>
              <FooterLink>
              <Link1 
              href="https://github.com/ssantoshp/Empyrial/wiki" 
              target="_blank" 
              rel="noreferrer">
              Docs</Link1></FooterLink>
            </FooterLinkItems>
            <FooterLinkItems>
              <FooterLinkTitle>Contribute</FooterLinkTitle>
              <FooterLink>
              <Link1 
              href="https://github.com/ssantoshp/Empyrial/discussions"
              target="_blank"
              rel="noreferrer"
              >Discussion</Link1>
              </FooterLink>
              <FooterLink>
              <Link1
              href="https://github.com/ssantoshp/Empyrial/issues"
              target="_blank"
              rel="noreferrer"
              >Issues</Link1></FooterLink>
            </FooterLinkItems>
          </FooterLinksWrapper>
        </FooterLinksContainer>
      </FooterWrap>
    </FooterContainer>
  )
}

export default Footer;
