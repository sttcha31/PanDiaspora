"use client";

import React, { useEffect } from 'react';
import * as d3 from 'd3';
import { Types } from './types';

const BasicBarChart = (props: IBasicBarChartProps) => {
  useEffect(() => {
    draw()
  })

  const draw = () => {
    const width = props.width - props.left - props.right
    const height = props.height - props.top - props.bottom

    const x = d3.scaleBand().range([0, width]).padding(0.1)
    const y = d3.scaleLinear().range([height, 0])

    const svg = d3
      .select('.basicBarChart')
      .append('svg')
      .attr('width', width + props.left + props.right)
      .attr('height', height + props.top + props.bottom)
      .append('g')
      .attr('transform', `translate(${props.left},${props.top})`)

    d3.dsv(',', props.file, (d) => {
      return (d as unknown) as Types.Data
    }).then((data) => {
      // Scale the range of the Data in the domains
      x.domain(
        data.map((d) => {
          return d.year
        })
      )
      y.domain([
        0,
        d3.max(data, (d) => {
          return Math.max(...data.map((dt) => (dt as Types.Data).frequency), 0)
        }),
      ] as number[])

      svg
        .selectAll('.bar')
        .data(data)
        .enter()
        .append('rect')
        .attr('fill', props.fill)
        .attr('class', 'bar')
        .attr('x', (d) => {
          return x(d.year) || 0
        })
        .attr('width', x.bandwidth())
        .attr('y', (d) => {
          return y(d.frequency)
        })
        .attr('height', (d) => {
          return height - y(d.frequency)
        })

      // add the x Axis
      svg.append('g').attr('transform', `translate(0,${height})`).call(d3.axisBottom(x))

      // add the y Axis
      svg.append('g').call(d3.axisLeft(y))

      svg.append("text")
        .attr("class", "x label")
        .attr("text-anchor", "end")
        .attr("x", width / 2)
        .attr("y", height + props.top + 30)
        .text("Year");
      
        svg.append("text")
          .attr("class", "y label")
          .attr("text-anchor", "end")
          .attr('x', 0 - height / 4)
          .attr('y', -props.left)
          .attr("dy", ".75em")
          .attr("transform", "rotate(-90)")
          .text("Frequency of Pubication");
    })
  }

  return <div className="basicBarChart" />
}

interface IBasicBarChartProps {
  width: number
  height: number
  top: number
  right: number
  bottom: number
  left: number
  fill: string
  file: string
  xaxis: string
  yaxis: string
}

export default BasicBarChart