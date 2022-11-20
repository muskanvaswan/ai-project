import { Box, Typography, Button, Chip } from '@mui/material'
import React from "react"

export default function Component() {
  
  const [ article, setArticle ] = React.useState({
    "headline": "",
    "summary": "",
    "image_url": ""
  })

  React.useEffect(() => {
    fetch("http://127.0.0.1:5000")
      .then((res) => res.json())
      .then((data) => setArticle(data))
  }, [])

  return (
    <Box sx={{
        width: "100%", 
        height: "80vh", 
        display: "flex", 
        alignItems: "center", 
        justifyContent: "center", 
        flexDirection: "column",
        p: 5,
        m: 2,
        borderRadius: 5,
        background: "#000000 box, linear-gradient(to right top, #3687ff, #5579fa, #6f69f2, #8655e7, #9b3cd8) border-box",
        backgroundClip: "padding-box",
        boxSizing: "border-box",
        borderWidth: 2,
        borderColor: "transparent",
        borderStyle: "solid",
        bgcolor: "#000000",
        position: "relative",
        "&:before": {
            content: "''",
            position: "absolute",
            top: 0,
            right: 0,
            bottom: 0,
            left: 0,
            zIndex: -1,
            margin: '-1px',
            borderRadius: "inherit",
            background: "linear-gradient(to right top, #3687ff, #5579fa, #6f69f2, #8655e7, #9b3cd8)"
        }
    }}>
      <Box 
        component="img" 
        sx={{
          borderRadius: 5, 
          mb: 2
        }}
        src={article.image_url} width="100%" height="100%"/>
      <Typography variant="h5" gutterBottom>{article.headline}</Typography>
      {/* <Chip label="Positive" sc={{background: "linear-gradient(to right top, #3687ff, #5579fa, #6f69f2, #8655e7, #9b3cd8)", p: 5}}/> */}
      <Typography 
        variant="body2"
        dangerouslySetInnerHTML={{__html: article.summary}}>
      </Typography>
      <Box sx={{
        height: 20,
        width: "100%",
        display: "flex",
        alignItems: "center",
        justifyContent: "flex-end",
        pt: 5
      }}>
        <Button 
          variant="contained" 
          sx={{
            borderRadius: 4, 
            width: "40%",
            background: "linear-gradient(to right top, #3687ff, #5579fa, #6f69f2, #8655e7, #9b3cd8)"
          }}>Positive </Button>
      </Box>
    </Box>
  )
}
