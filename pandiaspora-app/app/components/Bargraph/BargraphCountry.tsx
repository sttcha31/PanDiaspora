"use client";

import React, { useEffect } from 'react';
import * as d3 from 'd3';
import { Types } from './types';

const BargraphCountry = (props: BargraphCountryProps) => {
  useEffect(() => {
    draw()
  })

  const draw = () => {
    const width = props.width - props.left - props.right
    const height = props.height - props.top - props.bottom

    const x = d3.scaleBand().range([0, width]).padding(0.1)
    const y = d3.scaleLinear().range([height, 0])

    const xaxisLabel = props.xaxis;
    const tooltip = d3.select('.basicBarChart')
      .append('div')
      .attr('class', 'tooltip')
      .style('opacity', 0);
    const svg = d3
      .select('.barGraphCountry')
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
          return d.x
        })
      )
      y.domain([
        0,
        d3.max(data, (d) => {
          return Math.max(...data.map((dt) => (dt as Types.Data).y), 0)
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
          return x(d.x) || 0
        })
        .attr('width', x.bandwidth())
        .attr('y', (d) => {
          return y(d.y)
        })
        .attr('height', (d) => {
          return height - y(d.y)
        })
        .on("mouseenter", function (event, d) {
          if (d.x) {
            const xPosition = x(d.x) + x.bandwidth() / 2;
            const yPosition = y(d.y) - 10; // Adjust the positioning
      
            svg.append('text')
              .attr('class', 'value-label')
              .attr('x', xPosition)
              .attr('y', yPosition)
              .attr('text-anchor', 'middle')
              .attr('font-size', '12px')
              .attr('fill', 'black')
              .text(d.y); // Display the value of the bar
      
            // Additional actions you want to perform on mouseover
          } // Adjust the positioning
          d3.select(event.currentTarget)
            .attr('fill', 'orange');
        })
        .on('mouseout', (event, d) => {
          svg.selectAll('.value-label').remove();
          d3.select(event.currentTarget)
          .attr('fill', props.fill)
          .text(d.y); // Restore the original color
        });
      
          // this is only part of the implementation, check the source code

      // add the x Axis
      svg
      .append('g')
      .attr('transform', `translate(0,${height})`)
      .call(d3.axisBottom(x))
      .selectAll('.tick text') // Select all x-axis labels
      .style('text-anchor', 'end')
      .attr('dx', '-.8em')
      .attr('dy', '.15em')
      .attr('transform', 'rotate(-45)')
      .style('font-size', '12px');

      // add the y Axis
      svg.append('g').call(d3.axisLeft(y))

      svg.append("text")
        .attr("class", "x label")
        .attr("text-anchor", "end")
        .attr("x", width / 2)
        .attr("y", height + props.top + 80)
        .text(xaxisLabel);
      
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

  return <div className="barGraphCountry" />
}

interface BargraphCountryProps {
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

export default BargraphCountry