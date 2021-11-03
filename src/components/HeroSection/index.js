import React, {useState} from 'react';                                                      
import Video from '../../videos/video.jpeg';
import { Button } from '../ButtonElements';
import  { 
  HeroContainer, 
  HeroBg, 
  VideoBg,
  HeroContent,
  HeroH1,
  HeroP,
  HeroBtnWrapper,
  ArrowForward,
  ArrowRight,
  Link
} from './HeroElements';

                                                                                 
const HeroSection = () => {                                                    
  const [hover, setHover] = useState(false)

  const onHover = () => {
    setHover(!hover)
  }

  return (                                                                    
    <HeroContainer id="home">
      <HeroBg>
        <VideoBg src={Video} type='image/jpeg' />
      </HeroBg>
      <HeroContent>
        <HeroH1>Empyrial</HeroH1>
        <HeroP>
          Python-based open source AI and data-driven quantitative portfolio management for risk and performance analytics
        </HeroP>
        <HeroBtnWrapper>
          <Button to='/contact'
            onMouseEnter={onHover} 
            onMouseLeave={onHover}
            primary='true'
            dark='true'
          ><Link href='https://github.com/ssantoshp/Empyrial/archive/HEAD.zip'>
            Download {hover ? <ArrowForward /> : <ArrowRight />}
          </Link></Button>
        </HeroBtnWrapper>
      </HeroContent>
    </HeroContainer>
  );     
 };                                                                               
                                                                               
export default HeroSection;
