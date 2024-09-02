/** @odoo-module */
import {Component, useState, useSubEnv} from "@odoo/owl";
import {getDefaultConfig} from "@web/views/view";
import {registry} from "@web/core/registry";

export class G2PSupersetDashboard extends Component {
    async setup() {
        this.state = useState({
            isLoading: true,
            cookieService: null,
        });

        useSubEnv({
            config: {
                ...getDefaultConfig(),
                ...this.env.config,
            },
        });

        const orm = this.env.services.orm;
        this.getSupersetUrl(orm);
    }

    async getSupersetUrl(orm) {
        const data = await orm.searchRead(
            "ir.config_parameter",
            [["key", "=", "g2p_superset_dashboard.superset_url"]],
            ["value"]
        );

        if (data && data.length > 0 && data[0].value) {
            this.superSetUrl = data[0].value;
        } else {
            this.superSetUrl = false;
        }

        this.state.isLoading = false;
    }
}

G2PSupersetDashboard.template = "g2p_superset_dashboard.G2PSupersetDashboard";
registry.category("actions").add("g2p.superset_dashboard", G2PSupersetDashboard);
