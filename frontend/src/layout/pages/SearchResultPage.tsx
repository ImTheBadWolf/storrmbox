import React from 'react';
import { withRouter, RouteComponentProps } from 'react-router-dom';
import MediaCardList from '../MediaCardList';
import { observer } from 'mobx-react';
import SearchStore from '../../stores/SearchStore';

type SRPProps = RouteComponentProps<{ query: string }>;

@observer
class SearchResultPage extends React.Component<SRPProps> {

    componentDidUpdate(prevProps: SRPProps) {
        if (prevProps.match.params.query !== this.props.match.params.query) {
            SearchStore.runSearch(this.props.match.params.query);
        }
    }

    componentDidMount() {
        SearchStore.runSearch(this.props.match.params.query);
    }

    render() {
        if (SearchStore.fetching) {
            return <p className="pt-5 text-center">Searching...</p>;
        }

        return <>
            <h3 className="pt-5">Search results:</h3>
            <MediaCardList uidList={SearchStore.results} />
        </>
    }
}

export default withRouter(SearchResultPage);