// Type definitions for particles-bg 2.4.0
// Project: https://github.com/lindelof/particles-bg
// Definitions by: Dragoș Străinu https://github.com/strdr4605

import React from 'react';

declare module "particles-bg" {

  export type ConfigPositionProp = any;
  // Some typing error actual type should be:

  // export type ConfigPositionProp =
  // | "center"
  // | "all"
  // | { x: number; y: number; width: number; height: number }
  export interface ConfigProp {
    num: number[];
    rps: number;
    radius: number[];
    life: number[];
    v: number[];
    tha: number[];
    body?: string;
    rotate?: number[];
    alpha: number[];
    scale: number[];
    position: ConfigPositionProp;
    color: string[];
    cross: string;
    random: number | null;
    g: number;
    f?: number[];
    onParticleUpdate?: (ctx: any, particle: any) => void;
  }

  export type TypeProp =
  | "color"
  | "ball"
  | "lines"
  | "thick"
  | "circle"
  | "cobweb"
  | "polygon"
  | "square"
  | "tadpole"
  | "fountain"
  | "random"
  | "list"
  | "custom";

  export interface Props {
    type?: TypeProp;
    num?: number;
    bg?: boolean;
    color?: string;
    config?: ConfigProp;
  }

  class ParticlesBg extends React.Component<Props, any> {}

  export default ParticlesBg;
}
