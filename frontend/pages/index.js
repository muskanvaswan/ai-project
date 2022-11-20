import * as React from 'react';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';

import Component from '../src/components/Component'

export default function Index() {
  return (
    <Container maxWidth="sm" sx={{display: "flex", justifyContent: "center", alignItems: "center", flexDirection: "column", height: "100vh"}}>
      <Component />
    </Container>
  );
}
