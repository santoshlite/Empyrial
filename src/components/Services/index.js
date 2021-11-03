import React from 'react';
import {
  ServicesContainer,
  ServicesH1,
  ServicesWrapper,
  ServicesCard,
  ServicesIcon,
  ServicesH2,
  ServicesP
} from './ServicesElements';
import Icon1 from '../../images/svg-4.svg';
import Icon2 from '../../images/svg-5.svg';
import Icon3 from '../../images/svg-6.svg';
import Icon4 from '../../images/svg-7.svg';


const Services = () => {
  return (
    <ServicesContainer id="services">
      <ServicesH1>By Investors, For Investors.</ServicesH1>
      <ServicesWrapper>
        <ServicesCard>
          <ServicesIcon src={Icon1} />
          <ServicesH2>Multi-approach</ServicesH2>
          <ServicesP>
            From fundamental analysis to quantitative analysis and prediction generation, Empyrial offers a wide range of analysis so you can get the best insight from your investments
          </ServicesP>
        </ServicesCard>
        <ServicesCard>
          <ServicesIcon src={Icon2} />
          <ServicesH2>AI and data-driven</ServicesH2>
          <ServicesP>
            Empyrial empowers individual and financial institutions with AI and data so they can tackle the biggest challenges on the financial market
          </ServicesP>
        </ServicesCard>
        <ServicesCard>
          <ServicesIcon src={Icon3} />
          <ServicesH2>Flexible</ServicesH2>
          <ServicesP>
            Combining multiple librairies and data sources, Empyrial adapts to your needs so you can develop and evolve your strategies faster
          </ServicesP>
        </ServicesCard>
        <ServicesCard>
          <ServicesIcon src={Icon4} />
          <ServicesH2>Open source</ServicesH2>
          <ServicesP>
            Follows the most open MIT open source protocol, get all the project source code on Github, free to use for open source and commerical projects, forever
          </ServicesP>
        </ServicesCard>
      </ServicesWrapper>
    </ServicesContainer>
  );
};

export default Services;
