import React from "react"

import styles from "./responsiveCard.css"
import Card from "../common/Card";

const ResponsiveCard = props => (
    <div className={styles.card}>
        <Card {...props} />
    </div>
)

export default ResponsiveCard